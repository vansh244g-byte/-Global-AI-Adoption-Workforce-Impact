import pandas as pd
import seaborn as  sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import statsmodels as sn

df =pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\mini project\ai_tool_usage.csv')

df['respondent_id']= df['productivity_change_pct'].fillna(df['satisfaction_score'].median())
tool_count = df['ai_tool'].value_counts().reset_index()
tool_count.columns =['ai_tool','count']


satisfaction = df['satisfaction_score'].value_counts().sort_index().reset_index()

fig = px.bar(
    satisfaction,
    x='satisfaction_score',
    y='count',
    title='AI Tool Satisfaction Score'
)


st.plotly_chart(fig)