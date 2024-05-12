import joblib
import re
from utils.feature_functions import *


def prediction_data_prep(dataframe):
    pd.set_option('future.no_silent_downcasting', True)

    dataframe = dataframe.drop(["Booking_ID", "P-C", "P-not-C"], axis=1)

    # Converting 'booking status' to numerical values
    dataframe['booking status'] = dataframe['booking status'].replace({'Canceled': 1, 'Not_Canceled': 0}).astype(
        int).infer_objects(copy=False)

    # Converting 'date of reservation' to datetime format and filtering out null values and dates before 2017-06-30
    dataframe["date of reservation"] = pd.to_datetime(dataframe["date of reservation"], format="%m/%d/%Y",
                                                      errors='coerce')
    dataframe = dataframe.dropna(axis=0)
    dataframe = dataframe[dataframe['date of reservation'] > '2017-06-30']

    # Filtering out rows with 'type of meal' as "Meal Plan 3"
    dataframe = dataframe[dataframe["type of meal"] != "Meal Plan 3"]

    # Enter column names by type
    cat_cols = ['type of meal', 'room type', 'market segment type', 'number of adults', 'number of children', 'car parking space', 'repeated', 'special requests', 'booking status']
    num_cols = ['number of weekend nights', 'number of week nights', 'lead time', 'average price', 'date of reservation']
    cat_but_car = []

    # Moving numeric columns that contain "number" to 'num_cols'
    for col in cat_cols.copy():
        if re.search(r"number", str(col)):
            num_cols.append(col)
            cat_cols.remove(col)

    # Creating new columns: 'total number of customers', 'number of total nights', 'total price'
    dataframe["total number of customers"] = dataframe["number of adults"] + dataframe["number of children"]
    dataframe["number of total nights"] = dataframe["number of weekend nights"] + dataframe["number of week nights"]
    dataframe["total price"] = dataframe["number of total nights"] * dataframe["average price"]

    # Creation of the 'guest type' column
    dataframe['guest type'] = [
        'only children' if adult == 0 and child > 0 else
        'single' if adult == 1 and child == 0 else
        'couple' if adult == 2 and child == 0 else
        'family' if adult > 0 and child > 0 else
        'a group of guest' if adult > 2 and child == 0 else
        ''  # default value
        for adult, child in zip(dataframe['number of adults'], dataframe['number of children'])
    ]

    # Creation of the 'night type' column
    dataframe['night type'] = [
        'daily' if weekend == 0 and week == 0 else
        'only weekdays' if weekend == 0 and week != 0 else
        'only weekends' if weekend != 0 and week == 0 else
        'mixed' if weekend != 0 and week != 0 else
        ''  # default value
        for weekend, week in zip(dataframe['number of weekend nights'], dataframe['number of week nights'])
    ]

    # Creating new columns: 'date of transaction', 'reservation month', 'reservation season', 'transaction month', 'transaction season'
    dataframe['date of transaction'] = dataframe['date of reservation'] - pd.to_timedelta(dataframe['lead time'],
                                                                                          unit='d')
    dataframe['reservation month'] = dataframe['date of reservation'].dt.month_name()
    dataframe['reservation season'] = dataframe['date of reservation'].apply(determine_season)
    dataframe['transaction month'] = dataframe['date of transaction'].dt.month_name()
    dataframe['transaction season'] = dataframe['date of transaction'].apply(determine_season)

    # Creating new columns with range labels: 'Average Price Range', 'lead time Range'
    average_price_bins = [-1, 1, 50, 100, 200, 500]
    average_price_labels = ["Free", 'Less than 50', '50 - 100', "100 - 199", "200 and above"]
    dataframe['Average Price Range'] = pd.cut(dataframe['average price'], bins=average_price_bins,
                                              labels=average_price_labels, right=False)

    lead_time_bins = [-1, 92, 183, 274, 500]
    lead_time_labels = ["0-3 months", '3-6 months', '6-9 months', "over 9 months"]
    dataframe['lead time Range'] = pd.cut(dataframe['lead time'], bins=lead_time_bins, labels=lead_time_labels,
                                          right=False)

    # Dropping unnecessary columns
    dataframe = dataframe.drop(["date of reservation", "date of transaction"], axis=1)

    # Enter column names by type
    cat_cols = ['type of meal', 'room type', 'market segment type', 'number of adults', 'number of children', 'car parking space', 'repeated', 'special requests', 'booking status']
    num_cols = ['number of weekend nights', 'number of week nights', 'lead time', 'average price']
    cat_but_car = []

    # Moving numeric columns that contain "number" to 'num_cols'
    num_cols += [col for col in cat_cols if re.search(r"number", col)]
    cat_cols = [col for col in cat_cols if col not in num_cols]

    # Dropping highly correlated columns from numeric columns
    drop_list = high_correlated_cols(dataframe[num_cols])
    dataframe = dataframe.drop(drop_list, axis=1)

    # One-hot encoding for categorical columns with 2 < unique values <= 12
    ohe_cols = ['type of meal', 'room type', 'market segment type', 'guest type', 'night type', 'reservation month', 'reservation season', 'transaction month', 'transaction season', 'special requests', 'Average Price Range', 'lead time Range']
    dataframe = pd.get_dummies(dataframe, columns=ohe_cols, drop_first=True, dummy_na=True)

    # # Enter column names by type
    # cat_cols = ['number of adults', 'number of children', 'number of weekend nights', 'car parking space', 'repeated', 'booking status', 'type of meal_Meal Plan 2', 'type of meal_Not Selected', 'type of meal_nan', 'room type_Room_Type 2', 'room type_Room_Type 3', 'room type_Room_Type 4', 'room type_Room_Type 5', 'room type_Room_Type 6', 'room type_Room_Type 7', 'room type_nan', 'market segment type_Complementary', 'market segment type_Corporate', 'market segment type_Offline', 'market segment type_Online', 'market segment type_nan', 'guest type_couple', 'guest type_family', 'guest type_only children', 'guest type_single', 'guest type_nan', 'night type_mixed', 'night type_only weekdays', 'night type_only weekends', 'night type_nan', 'reservation month_August', 'reservation month_December', 'reservation month_February', 'reservation month_January', 'reservation month_July', 'reservation month_June', 'reservation month_March', 'reservation month_May', 'reservation month_November', 'reservation month_October', 'reservation month_September', 'reservation month_nan', 'reservation season_Spring', 'reservation season_Summer', 'reservation season_Winter', 'reservation season_nan', 'transaction month_August', 'transaction month_December', 'transaction month_February', 'transaction month_January', 'transaction month_July', 'transaction month_June', 'transaction month_March', 'transaction month_May', 'transaction month_November', 'transaction month_October', 'transaction month_September', 'transaction month_nan', 'transaction season_Spring', 'transaction season_Summer', 'transaction season_Winter', 'transaction season_nan', 'special requests_1.0', 'special requests_2.0', 'special requests_3.0', 'special requests_4.0', 'special requests_5.0', 'special requests_nan', 'Average Price Range_Less than 50', 'Average Price Range_50 - 100', 'Average Price Range_100 - 199', 'Average Price Range_200 and above', 'Average Price Range_nan', 'lead time Range_3-6 months', 'lead time Range_6-9 months', 'lead time Range_over 9 months', 'lead time Range_nan']
    # num_cols = ['number of week nights', 'lead time', 'average price']
    # cat_but_car = []
    #
    # # Moving numeric columns that contain "number" to 'num_cols'
    # num_cols += [col for col in cat_cols if re.search(r"number", col)]
    # cat_cols = [col for col in cat_cols if col not in num_cols]
    #
    # # Robust scaling for numeric columns
    # # rs = RobustScaler()
    # rs = joblib.load('robust_scaler.pkl')
    # dataframe[num_cols] = rs.transform(dataframe[num_cols])

    # column names of the main data set
    A_column_names = ['number of adults', 'number of children', 'number of weekend nights',
                      'number of week nights', 'car parking space', 'lead time', 'repeated',
                      'average price', 'booking status', 'type of meal_Meal Plan 2',
                      'type of meal_Not Selected', 'type of meal_nan',
                      'room type_Room_Type 1', 'room type_Room_Type 2',
                      'room type_Room_Type 4', 'room type_Room_Type 6', 'room type_nan',
                      'market segment type_Corporate', 'market segment type_Offline',
                      'market segment type_Online', 'market segment type_Rare',
                      'market segment type_nan', 'guest type_a group of guest',
                      'guest type_couple', 'guest type_family', 'guest type_single',
                      'guest type_nan', 'night type_mixed', 'night type_only weekdays',
                      'night type_only weekends', 'night type_nan',
                      'reservation month_August', 'reservation month_December',
                      'reservation month_February', 'reservation month_January',
                      'reservation month_July', 'reservation month_June',
                      'reservation month_March', 'reservation month_May',
                      'reservation month_November', 'reservation month_October',
                      'reservation month_September', 'reservation month_nan',
                      'reservation season_Spring', 'reservation season_Summer',
                      'reservation season_Winter', 'reservation season_nan',
                      'transaction month_August', 'transaction month_December',
                      'transaction month_February', 'transaction month_January',
                      'transaction month_July', 'transaction month_June',
                      'transaction month_March', 'transaction month_May',
                      'transaction month_November', 'transaction month_October',
                      'transaction month_September', 'transaction month_nan',
                      'transaction season_Spring', 'transaction season_Summer',
                      'transaction season_Winter', 'transaction season_nan',
                      'special requests_1.0', 'special requests_2.0', 'special requests_3.0',
                      'special requests_4.0', 'special requests_5.0', 'special requests_nan',
                      'Average Price Range_Less than 50', 'Average Price Range_50 - 100',
                      'Average Price Range_100 - 199', 'Average Price Range_200 and above',
                      'Average Price Range_nan', 'lead time Range_3-6 months',
                      'lead time Range_6-9 months', 'lead time Range_over 9 months',
                      'lead time Range_nan']
    A = pd.DataFrame(columns=A_column_names)
    A_columns = A.columns

    dataframe2 = dataframe.reindex(columns=A_columns, fill_value=False)
    dataframe2 = dataframe2.fillna(False)
    missing_columns = [col for col in dataframe2.columns if col not in A_columns]
    dataframe2 = dataframe2.drop(columns=missing_columns)

    X_selected_df = dataframe2[['number of adults', 'number of weekend nights', 'number of week nights',
                       'car parking space', 'lead time', 'repeated', 'average price',
                       'type of meal_Not Selected', 'room type_Room_Type 4',
                       'market segment type_Corporate', 'market segment type_Offline',
                       'market segment type_Online', 'guest type_couple', 'guest type_single',
                       'night type_mixed', 'night type_only weekdays',
                       'reservation month_December', 'reservation month_February',
                       'reservation month_January', 'reservation month_July',
                       'reservation month_March', 'reservation month_May',
                       'reservation month_November', 'reservation month_October',
                       'reservation month_September', 'reservation season_Summer',
                       'reservation season_Winter', 'transaction month_December',
                       'transaction month_January', 'transaction season_Spring',
                       'transaction season_Summer', 'special requests_1.0',
                       'special requests_2.0', 'special requests_3.0', 'special requests_4.0']].copy()

    new_model = joblib.load("model/lgbm.pkl")
    prediction = new_model.predict(X_selected_df)

    return prediction