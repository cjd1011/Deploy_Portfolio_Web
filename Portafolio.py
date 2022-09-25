#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install openpyxl
import pandas as pd #pip install pandas
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit

import datetime #pip install datetime

import pickle 
from pathlib import Path #pip install pathlib

import altair as alt #pip install altair
import plotly.graph_objects as go #pip install plotly
import streamlit_authenticator as stauth #pip install streamlit-authenticator

st.set_page_config(
     page_title="Investment Portfolio",
     page_icon=":moneybag",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )


st.title("Investment Portfolio")

st.markdown("##")

df = pd.read_excel('Portafolio.xlsx')

Activo = st.selectbox(
        "Seleccione el Activo:",
        options = df['Asset'].unique(),
        #default = "USD/COP" #Aqui podría por default dejar un filtro especifico pero vamos a dejarlos todos puestos por default
    )

df_seleccion = df.query("Asset ==@Activo ")

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])


tab1.subheader("Asset Chart")

fig1 = go.Figure(data=[go.Candlestick(x=df_seleccion['Date'],
                open=df_seleccion['Open'],
                high=df_seleccion['High'],
                low=df_seleccion['Low'],
                close=df_seleccion['Close'])])

fig1.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


tab1.write(fig1)

tab2.subheader("Asset Database")

tab2.write(df_seleccion)

#st.dataframe(df_seleccion)






     
                                




























                     
                     
