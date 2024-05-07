import streamlit as st
import cv2
import random
import pandas as pd
from st_pages import Page, show_pages
from utils import simulation_utils, page_utils
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

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

st.set_page_config(layout="wide")

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
# Coordinate dictionary
coordinates = {
    "room1": (454, 199),
    "room2": (511, 199),
    "room3": (568, 199),
    "room4": (395, 360),
    "room5": (453, 360),
    "room6": (512, 360),
    "room7": (569, 360),
    "room8": (625, 360),
    "room9": (395, 481),
    "room10": (453, 481),
    "room11": (512, 481),
    "room12": (569, 481),
    "room13": (625, 481),
    "room14": (395, 606),
    "room15": (453, 606),
    "room16": (512, 606),
    "room17": (569, 606),
    "room18": (625, 606),
    "room19": (395, 729),
    "room20": (453, 729),
    "room21": (512, 729),
    "room22": (569, 729),
    "room23": (625, 729),
    "room24": (395, 852),
    "room25": (453, 852),
    "room26": (512, 852),
    "room27": (569, 852),
    "room28": (625, 852),
    "room29": (395, 973),
    "room30": (453, 973),
    "room31": (512, 973),
    "room32": (569, 973),
    "room33": (625, 973),
    "room34": (395, 1094),
    "room35": (453, 1094),
    "room36": (512, 1094),
    "room37": (569, 1094),
    "room38": (625, 1094),
    # Add other coordinates here
}

# A predefined background image
background_path = r"assets/images/hilal.gif"  # Specifying a file path using a raw string

# Load the image to paste
overlay_path = "assets/images/windows/1.png"
overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
overlay = cv2.cvtColor(overlay, cv2.COLOR_BGRA2RGBA)  # Convert from BGRA to RGBA

result_image_path = "assets/images/hilal.png"
result_image = cv2.imread(result_image_path, cv2.IMREAD_UNCHANGED)
result_image = cv2.cvtColor(result_image, cv2.COLOR_BGRA2RGBA)  # Convert from BGRA to RGBA

# # Load model
# model_path = "model/voting_clf.pkl"
# model = load(model_path)

# Load iris data set
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train the model
model = RandomForestClassifier()
model.fit(df, y)

# # Load the CSV file
# df = pd.read_csv("data/booking.csv")

if 'page' not in st.session_state:
    st.session_state.page = 0

if 'random_df' not in st.session_state:
    st.session_state.random_df = None  # Initialize it as None

ph = st.empty()

tab1, tab2 = st.tabs(["____", "____"])

with ph.container():
    with tab1:
        col1, col2 = st.columns([1, 4])

        with col1:
            if st.session_state.page == 0:
                st.subheader("HOTEL MERT")
                st.image(background_path, use_column_width=True)
                st.button("Generate Random Data", on_click=page_utils.second_page)

            elif st.session_state.page == 1:
                st.session_state.random_df = pd.DataFrame(simulation_utils.random_data(df))
                num_to_paste = random.randint(1, len(coordinates))
                selected_coordinate = random.sample(list(coordinates.values()), num_to_paste)

                # Create and temporarily store the image
                result_image = simulation_utils.generate_result_image(result_image, overlay, selected_coordinate)

                # Put the new image
                st.subheader("HOTEL MERT")
                st.image("assets/images/generated_data.jpg", use_column_width=True)
                st.button("Generate Random Data", on_click=page_utils.second_page)
                st.button("Make Predictions", on_click=page_utils.third_page)

            elif st.session_state.page == 2:
                try:
                    # Make predictions
                    predictions = model.predict(st.session_state.random_df)

                    # Select non-0 from the predictions
                    non_zero_predictions = predictions[predictions != 0]

                    # Randomly select selected coordinates
                    selected_coordinate = random.sample(list(coordinates.values()), len(non_zero_predictions))

                    # Create and temporarily store the new image
                    result_image = simulation_utils.generate_result_image(result_image, overlay, selected_coordinate)

                    # Put the new image
                    st.subheader("HOTEL MERT")
                    st.image(result_image, caption=f"{len(non_zero_predictions)}", use_column_width=True)
                    st.button("Generate Random Data", on_click=page_utils.second_page)

                except ValueError as e:
                    # Catch the error and reset the page to 0
                    st.session_state.page = 0
                    st.subheader("HOTEL MERT")
                    st.image(background_path, use_column_width=True)
                    st.button("Generate Random Data", on_click=page_utils.second_page)

        with col2:
            if st.session_state.page == 0:
                st.subheader("Dataframe")
                st.write(df)

            elif st.session_state.page == 1:
                st.subheader("Generated random data:")
                st.write(st.session_state.random_df)

            elif st.session_state.page == 2:
                try:
                    # Add predictions as a new column to the DataFrame
                    st.session_state.random_df['Predictions'] = predictions
                    # View predictions
                    st.subheader("Data with Predictions:")
                    st.write(st.session_state.random_df)
                except ValueError as e:
                    # Catch the error and reset the page to 0
                    st.session_state.page = 0

    with tab2:
        script = """<div id = 'chat_inner'></div>"""
        st.markdown(script, unsafe_allow_html=True)


chat_plh_style = f"""
    <style>
        div[data-testid='stTabs']:has(div#chat_inner) {{
            background-color: rgba(253, 250, 248, 0.5);
            border-radius: 16px;
            padding: 16px; 
            width: 1300px;       
            margin: auto;
            padding-bottom: 50px;
    </style>
    """

st.markdown(chat_plh_style, unsafe_allow_html=True)

# Sayfa Footer HTML Kod Uygulaması
with open("assets/html/footer.html", "r", encoding="utf-8") as pred:
    footer_html = f"""{pred.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)