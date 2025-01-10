import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(layout='wide',page_title="price predictor")

with open('property.pkl', 'rb') as file:
    property=pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline=pickle.load(file)

st.header("Enter your inputs")

property_type=st.selectbox("Property Type",["flat","house"])

place=st.selectbox("Place",sorted(property['place'].unique().tolist()))

area=float(st.number_input("Area"))

furnishing_type=st.selectbox("Furnishing Type",sorted(property['furnishing_details'].unique().tolist()))

bedrooms=int(st.selectbox("Bedrooms",sorted(property['bedrooms'].unique().tolist())))

bathroom=float(st.selectbox("Bathroom",sorted(property['bathroom'].unique().tolist())))

balcony=float(st.selectbox("Balcony",sorted(property['balcony'].unique().tolist())))

if st.button("Predict"):
    # form a datarframe
    data=[[property_type,place,area,furnishing_type,bedrooms,bathroom,balcony]]
    columns=["property_type","place","area","furnishing_details","bedrooms","bathroom","balcony"]
    df=pd.DataFrame(data,columns=columns)

    # predict
    base_price=float(np.expm1(pipeline.predict(df))[0])
    low=round(base_price-0.25,2)
    high=round(base_price+0.25,2)

    # display
    st.text(f"The price of the {property_type} in {place} is between {low} Cr and {high} Cr.") 
    similar_property=property[(property['bedrooms']==bedrooms) & (property['property_type']==property_type) & (property['area']<area+100) & (property['area']>area-100)]
    st.subheader("Similar properties")
    st.dataframe(similar_property)
