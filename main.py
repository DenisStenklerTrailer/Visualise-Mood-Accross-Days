import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os

# Streamlit title
st.title("Diary Tone")

# Reading all files in the diary directory
files = os.listdir('diary')
analyzer = SentimentIntensityAnalyzer()

#init
positivity = []
negativity = []

# looping over the files in the diary folder and reading them
for file in files:
    with open(f"diary/{file}",'r') as file:
        data = file.read()

    # getting the negativity and positivity score
    scores = analyzer.polarity_scores(data)
    negativity.append(scores['neg'])
    positivity.append(scores['pos'])
    print(scores)

# plot for positivity
st.header("Positivity")
pos_figure = px.line(x=[date.strip(".txt") for date in files], y=positivity,labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

# plot for negativity
st.header("Negativity")
neg_figure = px.line(x=[date.strip(".txt") for date in files], y=negativity,labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(neg_figure)


