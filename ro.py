import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    filename = "social_media_3platforms_3years.csv"

    # Safety check for Streamlit Cloud
    if not os.path.exists(filename):
        st.error("CSV file not found in GitHub repo")
        st.stop()

    df = pd.read_csv(filename)

    # Engagement calculation
    df["engagement"] = df["likes"] + df["comments"] + df["shares"]

    # Assumed campaign cost (project purpose)
    df["campaign_cost"] = 5000

    # ROI calculation
    df["roi"] = ((df["engagement"] - df["campaign_cost"]) / df["campaign_cost"]) * 100

    return df

df = load_data()
