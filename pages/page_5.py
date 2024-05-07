import streamlit as st
from st_pages import Page, show_pages

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
ph = st.empty()

tab1, tab2 = st.tabs(["____", "____"])

with ph.container():
    with tab1:
        st.subheader("**About MAINSOFT: Hotel Booking Cancellation Prediction**")
        st.markdown(
            """
            

            MAINSOFT is an innovative data science and software company that provides solutions for businesses to leverage their data potential. We develop predictive models based on real-world data to empower our clients to make informed decisions.

            **Dataset Overview**

            We obtained our dataset from Kaggle, comprising a diverse range of features including booking details, customer information, and reservation specifics, meticulously gathered from real-world hotel booking scenarios to ensure authenticity and relevance.

            **Dataset Features**

            - **Booking_ID**: Unique identifier for each booking
            - **Number of Adults**: Number of adults included in the booking
            - **Number of Children**: Number of children included in the booking
            - **Number of Weekend Nights**: Number of weekend nights included in the booking
            - **Number of Week Nights**: Number of week nights included in the booking
            - **Type of Meal**: Type of meal included in the booking
            - **Car Parking Space**: Indicates whether a car parking space was requested or included in the booking
            - **Room Type**: Type of room booked
            - **Lead Time**: Number of days between the booking date and the arrival date
            - **Market Segment Type**: Type of market segment associated with the booking
            - **Repeated**: Indicates whether the booking is a repeat booking
            - **P-C**: Number of previous bookings that were canceled by the customer prior to the current booking
            - **P-not-C**: Number of previous bookings not canceled by the customer prior to the current booking
            - **Average Price**: Average price associated with the booking
            - **Special Requests**: Number of special requests made by the guest
            - **Date of Reservation**: Date of the reservation
            - **Booking Status**: Status of the booking (canceled or not canceled)

            This dataset can be used to predict the likelihood of hotel booking cancellations. Such predictions can assist hotel businesses in optimizing their resources and enhancing customer satisfaction.

            For more details, visit the [dataset link](https://www.kaggle.com/datasets/youssefaboelwafa/hotel-booking-cancellation-prediction/data).
            """
        )

    with tab2:
        script = """<div id = 'chat_inner'></div>"""
        st.markdown(script, unsafe_allow_html=True)


chat_plh_style = f"""
    <style>
        div[data-testid='stTabs']:has(div#chat_inner) {{
            background-color: rgba(253, 250, 248, 0.5);
            border-radius: 16px;
            padding: 16px; 
            padding-bottom: 32px;
            width: 800px;
            margin: auto;
    </style>
    """

st.markdown(chat_plh_style, unsafe_allow_html=True)

# Sayfa Footer HTML Kod Uygulaması
with open("assets/html/footer.html", "r", encoding="utf-8") as pred:
    footer_html = f"""{pred.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)