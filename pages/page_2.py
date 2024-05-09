import joblib
import streamlit as st
import pandas as pd
import random
from st_pages import Page, show_pages
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from utils import page_utils, preparation_df
from sklearn.feature_selection import RFE


st.set_page_config(layout="wide")

# Pages Design to Side Bar
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/page_1.py", "Data Analysis", "📊"),
        Page("pages/page_2.py", "Data Entry", "📟"),
        Page("pages/page_3.py", "Simulation", "🧪"),
        Page("pages/page_5.py", "About", "👩🏻‍💻"),
    ]
)

page_bg_img = f"""
<style>

    [data-testid="stAppViewContainer"] > .main {{
        background-color: #E1DAD6;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: local;
        }}

    [data-testid="stHeader"] {{
        background: rgba(80, 96, 121, 0.4);
        }}

    .st-ds  {{
        background-color: rgba(38, 39, 48, 0);
        }}

    [.data-testid="stColorBlock"] {{
        background-color: rgba(38, 39, 10);
        }}

    .st-emotion-cache-1aw8i8e {{
        color: #E1DAD6;
    }}

    [.data-testid="stSidebarNavLink"] {{
        color: white;
        }}
        
    .st-ds {{
        background-color: #D6E1E1;
        }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the width to your desired value
st.markdown(
    f"""
    <style>
        section[data-testid="stSidebar"] {{
            width: 200px !important; 
            background-color: #506079;

        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title and Font Style
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-family: Yellow peace;
            font-weight: lighter;
            color: rgba(43, 45, 49);
            font-size: 2.5rem;
            padding-bottom: 20px;
        }
        .me {
            text-align: center;
            font-family: Yellow peace;
            color: rgba(43, 45, 49);
            font-size: 1 rem;
            padding: 0;
            margin: 0;
        }

    </style>
""", unsafe_allow_html=True)

#####################################

old_data = pd.read_csv("data/booking.csv")

if 'page' not in st.session_state:
    st.session_state.page = 0

if 'random_df' not in st.session_state:
    st.session_state.random_df = None  # Initialize it as None

ph = st.empty()

tab1, tab2 = st.tabs(["Single Data Entry", "Multi Data Entry"])

with ph.container():
    with tab1:
        st.subheader("Single Data Entry")

        st.write("")

        cola, colb, colc, cold = st.columns(4)
        with cola:
            car_parking_space = st.checkbox("Parking Space", False, help="Does the customer request a car parking space?")

        with colb:
            special_request = st.checkbox("Special Request", False, help="Has the customer made special requests?")

        with colc:
            repeated = st.checkbox("Repeated", False, help="Is this a repeat booking?")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            lead_time = st.slider("Lead time", max_value=365, min_value=1, help="How far in advance did the customer book")
            adult = st.number_input("Number of adult", value=0, step=1, key="adult_input", help="Number of adult customers")
            week = st.number_input("Weekdays", value=0, step=1, key="weekdays_input", help="Number of days of stay on weekdays")

            meal_types = ["Not Selected", "Meal Plan 1", "Meal Plan 2"]

            selected_meal_type = st.selectbox(":black[Meal Type]", meal_types, help="Customer's meal type")
            selected_date = st.date_input("Select a date", value=None, min_value=None, max_value=None, key=None, help="Hotel reservation date")

        with col2:
            average_price = st.slider("Enter price", max_value=500, min_value=0, help="The average amount of money the customer pays for a day")
            kid = st.number_input("Number of children", value=0, step=1, key="kid_input", help="Number of child customers")
            weekend = st.number_input("Weekend Days", value=0, step=1, key="weekend_input", help="Number of days stayed at the weekend")

            room_types = ["Room Type 1", "Room Type 2", "Room Type 3", "Room Type 4", "Room Type 5", "Room Type 6",
                          "Room Type 7"]

            market_segment_type = ["Online", "Offline", "Corporate", "Complementary", "Aviation"]

            selected_market_segment_type = st.selectbox(":black[Market Segment]", market_segment_type, help="The way the customer carries out the purchase")

            selected_room_type = st.selectbox(":black[Room Type]", room_types, help="Customer's room type")

        st.write("")

        if st.button("Predict"):
            # Check the validity of all inputs
            if (car_parking_space and special_request and repeated and
                    lead_time > 0 and adult >= 0 and week >= 0 and selected_meal_type is not None and selected_date is not None and
                    average_price >= 0 and kid >= 0 and weekend >= 0 and
                    selected_market_segment_type is not None and selected_room_type is not None):
                # Estimate if all inputs are valid
                st.write("All inputs valid. Initiating prediction.")
                # Tahmin kodu buraya gelecek

                if special_request:
                    special_requests_value = random.randint(1, 5)  # 1 ile 5 arasında rastgele bir değer seçelim
                else:
                    special_requests_value = 0

                single_df = pd.DataFrame({
                    'Booking_ID': ["none"],
                    'number of adults': [adult],
                    'number of children': [kid],
                    'number of weekend nights': [weekend],
                    'number of week nights': [week],
                    'type of meal': [selected_meal_type],
                    'car parking space': [1 if car_parking_space else 0],
                    'room type': [f"{selected_room_type.split()[0]}_{selected_room_type.split()[1]} {selected_room_type.split()[2]}"],
                    'lead time': [lead_time],
                    'market segment type': [selected_market_segment_type],
                    'repeated': [1 if repeated else 0],
                    'P-C': ["none"],
                    'P-not-C': ["none"],
                    'average price': [average_price],
                    'special requests': [special_requests_value],
                    'date of reservation': [selected_date.strftime('%m/%d/%Y') if selected_date else None],
                    'booking status': [1]
                })

                single_df.to_csv('single_df.csv', index=False)
                prediction = preparation_df.booking_data_prep_for_prediction(old_data, single_df)

                # Ekrana yazdır
                single_df['Predictions'] = prediction
                single_df = single_df.drop(['Booking_ID', 'P-C', 'P-not-C', 'booking status'], axis=1)
                st.write(single_df)

                if prediction == 0:
                    st.subheader("**Hotel reservation will be :red[not cancelled]**")

                elif prediction == 1:
                    st.subheader("**Hotel reservation will be :red[cancelled]**")

            else:
                st.warning("Please fill in all entries or enter a valid value.")

    with tab2:
        if st.session_state.page == 0:
            # File upload
            uploaded_file = st.file_uploader("Upload a file", type=["csv"], key="file")
            # If file is uploaded
            if uploaded_file is not None:
                # Convert file to DataFrame
                try:
                    df = pd.read_csv(uploaded_file)
                except pd.errors.ParserError as e:
                    st.error("Error reading the file. Please make sure the file format is correct.")
                else:
                    # Check if uploaded data has the same features as iris dataset
                    if set(df.columns) != set(old_data.columns):
                        st.error("The uploaded data does not match the required format of the iris dataset.")
                    else:
                        # Perform the operations for predictions here
                        st.write("Uploaded Data:")
                        st.write(df)

                        # "Make Prediction" button
                        st.button("Make Prediction", on_click=page_utils.second_page)
            else:
                st.write("Please upload the file you want to predict above.")

        elif st.session_state.page == 1:
            # File upload
            uploaded_file = st.file_uploader("Upload a file", type=["csv"], key="file", on_change=page_utils.first_page)
            # Make predictions
            df = pd.read_csv(uploaded_file)
            predictions = preparation_df.booking_data_prep_for_prediction(old_data, df)

            # Add predictions as a new column to the DataFrame
            df['Predictions'] = predictions
            df = df.drop(['booking status'], axis=1)

            # Show DataFrame with predictions
            st.write("Data with Predictions:")
            st.write(df)

        script = """<div id = 'chat_inner'></div>"""
        st.markdown(script, unsafe_allow_html=True)


chat_plh_style = f"""
    <style>
        div[data-testid='stTabs']:has(div#chat_inner) {{
            background-color: rgba(253, 250, 248, 0.5);
            border-radius: 16px;
            padding: 16px; 
            width: 800px;       
            margin: auto;
    </style>
    """

st.markdown(chat_plh_style, unsafe_allow_html=True)

# Page Footer HTML Code Application
with open("assets/html/footer.html", "r", encoding="utf-8") as pred:
    footer_html = f"""{pred.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)
