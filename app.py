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


col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.image("assets/images/newlogo2.png")


# Sayfa Footer HTML Kod Uygulaması
with open("assets/html/footer.html", "r", encoding="utf-8") as pred:
    footer_html = f"""{pred.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)
