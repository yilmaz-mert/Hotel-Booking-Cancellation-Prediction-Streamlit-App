import streamlit as st
from st_pages import Page, show_pages
from streamlit.components.v1 import html
from utils.charts import create_chart, create_chart2, create_chart3, create_chart4, create_chart5, create_chart6

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
            # background-color: rgba(5, 29, 64, 0.7);
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

CHART = create_chart()
CHART2 = create_chart2()
CHART3 = create_chart3()
CHART4 = create_chart4()
CHART5 = create_chart5()
CHART6 = create_chart6()

ph = st.empty()
c1 = st.container()

# Define options for the drop-down menu
options = ['Booking Status', 'Lead Time Chart', 'Average Price Range', 'Guest Type', 'By Month', 'Market Segment']

# Specify the option to be shown by default (for example, "Option 1")
default_option_index = 0

with ph.container():
    tab1, tab2 = st.tabs(["____", "____"], )

    with tab1:
        st.header("Visualised Data For Analysis")

        # Create the drop-down menu and capture the selected value
        selected_option = st.selectbox('Select chart:', options, index=default_option_index,)

        if selected_option == "Lead Time Chart":
            st.subheader("Count Of Booking Status By Lead Time Range")
            # display Chart
            html(CHART, width=650, height=370)

            st.markdown(""" 
            ### Count of Booking Status by Lead Time Range

            The titled graph illustrates the number of bookings made across various lead time ranges, categorized based on booking status (canceled or not canceled).

            **Key Takeaways**

            - Examining the graph reveals that a substantial portion of bookings occur within 0-3 months of the guest's arrival date. This pattern aligns with the tendency of individuals to book their accommodations closer to their travel dates, allowing for more flexibility in case of unforeseen circumstances. Notably, a significant number of bookings are made further in advance, particularly within the 3-6 months and 6-9 months ranges. This indicates that some guests meticulously plan their trips well ahead of time and may secure their accommodations early to avail of favorable rates or ensure availability.

            - Interestingly, the graph highlights that a higher percentage of cancellations occur within the 6-9 months and 3-6 months lead time ranges. This trend could be attributed to various factors, including alterations in travel plans, budgetary constraints, or unexpected events. 
            """)

        elif selected_option == "Booking Status":
            st.subheader("Count Of Booking Status")
            # display Chart
            html(CHART2, width=650, height=370)

            st.markdown("""
                **Visual:** The provided data visualizes the distribution of booking statuses, categorized as "Not Canceled" and "Canceled".

                **Data:**
                
                - **Total Bookings:** 36239
                - **Not Canceled:** 24361 (67.2%)
                - **Canceled:** 11878 (32.8%)
                
                **Key Findings:**
                
                The majority of bookings (67.2%) are not canceled.
                A significant portion of bookings (32.8%) are canceled.
            """)

        elif selected_option == "Average Price Range":
            st.subheader("Count Of Booking Status By Average Price Range")
            # display Chart
            html(CHART3, width=650, height=370)

            st.markdown("""
                The graph illustrates the distribution of bookings across various average price ranges, categorized based on booking status (canceled or not canceled). Each bar segment represents the percentage of bookings within a specific price range and booking status category.

                **Key Observations**
                
                - **Price Range Distribution:** Analyzing the graph reveals that the most prevalent price range for bookings falls within the 50-100 range, accounting for approximately 40% of the total bookings. This suggests that a considerable portion of guests seek accommodations within this moderate price bracket. Following closely, the 100-199 price range holds a significant share of bookings, representing around 33% of the total. This indicates that a notable number of guests are willing to invest in slightly higher-priced accommodations.
                
                - **Booking Status Analysis:** Interestingly, the graph highlights that canceled bookings are more concentrated within the higher price ranges, particularly for the 200 and above category. This trend suggests that guests who book more expensive accommodations may be more likely to reconsider their reservations due to factors such as budget constraints or changes in travel plans.
            """)

        elif selected_option == "Guest Type":
            st.subheader("Count Of Booking Status By Guest Type")
            # display Chart
            html(CHART4, width=650, height=370)

            st.markdown("""
                The graph illustrates the distribution of bookings across various guest types, categorized based on booking status (canceled or not canceled). Each bar segment represents the percentage of bookings within a specific guest type and booking status category.

                **Key Observations**
                
                - **Guest Type Distribution:** Analyzing the graph reveals that the most prevalent guest type is couples, accounting for approximately 50% of the total bookings. This suggests that couples are a significant segment of the hotel's clientele. Following closely, single travelers hold a considerable share of bookings, representing around 18% of the total. This indicates that single travelers are also a notable target market for the hotel.
                
                - **Booking Status Analysis:** Interestingly, the graph highlights that canceled bookings are more concentrated among groups of guests and single travelers. This trend suggests that these guest types may be more likely to reconsider their reservations due to factors such as changes in travel plans or budgetary constraints.
            """)

        elif selected_option == "By Month":
            st.subheader("Count Of Booking Status By Month")
            # display Chart
            html(CHART5, width=650, height=370)

            st.write("""
            The illustration showcases the number of bookings made across various months, categorized based on booking status (canceled or not canceled). Each bar segment represents the total number of bookings for a specific month and booking status category.

            **Key Takeaways**
            
            - Examining the graph reveals a seasonal pattern in booking volume, with a significant surge in bookings during the summer months (June to August). This trend aligns with the tendency for individuals to plan vacations and leisure travel during warmer seasons. Notably, the peak booking months coincide with the highest occupancy rates, highlighting the importance of effective revenue management strategies during these periods.
            
            - Interestingly, the graph highlights that canceled bookings are more prevalent during the peak summer months (June to August). This trend could be attributed to various factors, including last-minute itinerary changes, inclement weather, or unforeseen circumstances.
            """)

        elif selected_option == "Market Segment":
            st.subheader("Count Of Booking Status By Market Segment")
            # display Chart
            html(CHART6, width=650, height=370)

            st.markdown("""
            The chart shows the number of bookings for each market segment (online, offline, corporate, aviation, complementary) broken down by booking status (canceled or not canceled).
            
            - **Market Segment with Highest Bookings:** Online bookings represent the highest volume of bookings among all market segments.

            - **Booking Status:**  For all market segments, there are more completed bookings (not canceled) than canceled bookings.
            
            - **Canceled Bookings by Market Segment:**  Among the canceled bookings, the highest proportions are for Aviation and Corporate bookings.
            """)

    with tab2:
        script = """<div id = 'chat_inner'></div>"""
        st.markdown(script, unsafe_allow_html=True)

chat_plh_style = f"""
    <style>
        div[data-testid='stTabs']:has(div#chat_inner) {{
            background-color: rgba(253, 250, 248, 0.5);
            border-radius: 16px;
            padding: 16px; 
            width: 700px;       
            margin: auto;
            padding-bottom: 50px;
    </style>
    """
st.markdown(chat_plh_style, unsafe_allow_html=True)

# Page Footer HTML Code Application
with open("assets/html/footer.html", "r", encoding="utf-8") as pred:
    footer_html = f"""{pred.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)

