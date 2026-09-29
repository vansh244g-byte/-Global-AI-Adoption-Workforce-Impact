import pandas as pd
import seaborn as  sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import statsmodels as sn

df =pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\mini project\salary_and_satisfaction.csv')
df["annual_salary_usd"]= df["salary_change_yoy_pct"].fillna(df["career_growth_outlook"].mode())

satisfaction = df['job_satisfaction_score'].value_counts().sort_index().reset_index()

fig = px.bar(
    satisfaction,
    x='job_satisfaction_score',
    y='count',
    title='Job Satisfaction Score'
)
st.plotly_chart(fig)