import pandas as pd
import seaborn as  sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import statsmodels as sn

df =pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\mini project\skills_and_training.csv')
df['skills']= df['num_skills'].fillna(df['weekly_learning_hours'].mode())

df['weekly_learning_hours'] = pd.to_numeric(
    df['weekly_learning_hours'],
    errors='coerce'
)

fig = px.histogram(
    df,
    x='weekly_learning_hours',
    title='Weekly Learning Hours'
)
st.plotly_chart(fig)