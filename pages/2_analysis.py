import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide',page_title="Real State Analysis")
st.title("Analytics")

new_df=pd.read_csv("dataset/data_viz1.csv")

group_df=new_df.groupby('place')[['price','price_per_sqft','area','latitude','longitude']].mean()

st.header("place price per sqft Geomap")
fig=px.scatter_mapbox(group_df,lat="latitude",lon="longitude",color="price_per_sqft",size="area",
                  color_continuous_scale=px.colors.cyclical.IceFire_r,zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)

st.header("Area Vs Price")

property_type=st.selectbox("Property Type",["flat","house"])

if property_type=="flat":
    fig1=px.scatter(new_df[new_df['property_type']=='flat'],x="area",y='price',color="bedrooms")
    st.plotly_chart(fig1,use_container_width=True)
else:
    fig1=px.scatter(new_df[new_df['property_type']=='house'],x="area",y='price',color="bedrooms")
    st.plotly_chart(fig1,use_container_width=True)

st.header("BHK Pie Chart")

place_options=new_df['place'].unique().tolist()
place_options.insert(0,"overall")

selected_place=st.selectbox("Select a place",place_options)

if selected_place=="overall":
    fig2=px.pie(new_df,names='bedrooms')
    st.plotly_chart(fig2,use_container_width=True)
else:
    fig2=px.pie(new_df[new_df['place']==selected_place],names='bedrooms')
    st.plotly_chart(fig2,use_container_width=True)

st.header("Side by Side BHK price comparison")

fig3=px.box(new_df[new_df['bedrooms']<=4],x="bedrooms",y="price",title='BHK Price Range')

st.plotly_chart(fig3,use_container_width=True)

st.header("Side by Side Distplot for property type")

fig4=plt.figure(figsize=(10,4))
sns.distplot(new_df[new_df['property_type']=='flat']["price"],label="Flat")
sns.distplot(new_df[new_df['property_type']=='house']["price"],label="House")
plt.legend()
st.pyplot(fig4)