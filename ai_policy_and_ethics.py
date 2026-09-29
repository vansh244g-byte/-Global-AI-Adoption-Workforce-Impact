import pandas as pd
import seaborn as  sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import statsmodels as sn

df =pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\mini project\ai_policy_and_ethics.csv')
df["company_has_ai_policy"]= df["data_privacy_concern_level"].fillna(df["ai_bias_concern_level"].median())

privacy = df['data_privacy_concern_level'].value_counts().reset_index()

fig = px.bar(
    privacy,
    x='data_privacy_concern_level',
    y='count',
    title='Data Privacy Concern Level',
    labels={
        'data_privacy_concern_level': 'Privacy Concern',
        'count': 'Number of Respondents'
    }
)

st.plotly_chart(fig)