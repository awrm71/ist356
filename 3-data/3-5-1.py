import pandas as pd
import streamlit as st

url = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'
exams = pd.read_csv(url)

st.dataframe(exams)
choices =  ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']
Method = st.selectbox('Select one of the methods:', choices)

grouped = exams.groupby(Method).agg({'Student_Score':['mean', 'count']})
st.dataframe(grouped)

# Create a streamlit to allow the user to select one of the following:

# - one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
# - after the selection is made display a dataframe that summarized the count of students and the average student score by the selection
