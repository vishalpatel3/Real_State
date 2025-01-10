import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout='wide',page_title="Real State Project")

st.title("Welcome to the Real State Project")
st.markdown("""
            Objective: This project aims to predict the price of houses based on various input features, such as the area of the house, the number of bedrooms, bathrooms, and other relevant factors. The goal is to provide an accurate and reliable price estimate for real estate properties, helping buyers, sellers, and investors make informed decisions in the real estate market.

Features:

Predictive Model: The core of the project is a machine learning model trained to predict house prices based on historical data.
User Input: Users can input property details like area, number of bedrooms, bathrooms, and other features, and the model will provide a predicted price.
Data Analysis: The project also includes data analysis capabilities, allowing users to upload property data and visualize key insights, such as the relationship between area and price.
Tech Stack:

Programming Language: Python
Machine Learning: Using models like Random Forest or XGBoost for price prediction.
Libraries: Streamlit for the web interface, Pandas for data manipulation, Matplotlib for visualizations.
Usage: You can input details such as area, number of bedrooms, and bathrooms, and the model will calculate and display the estimated price of the property. In addition, you can upload a dataset to perform analysis and gain insights into house prices.

Why This Project?: This project aims to make real estate predictions accessible to anyone interested in property investments or buying a new home. By utilizing machine learning techniques, we can provide fast and accurate predictions based on existing data."""    )