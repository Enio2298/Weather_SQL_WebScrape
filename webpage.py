import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("exercise.db")
cursor = connection.cursor()

cursor.execute("SELECT temperature, date FROM weather")
data = cursor.fetchall()


temperature = [item[0] for item in data]


date = [item[0] for item in data]


figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Temperature (°C)"})

st.plotly_chart(figure)