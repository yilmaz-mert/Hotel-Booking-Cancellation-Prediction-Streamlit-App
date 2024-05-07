import streamlit as st


def third_page():
    st.session_state.page = 2


def second_page():
    st.session_state.page = 1


def first_page():
    st.session_state.page = 0

