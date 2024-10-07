# ## Challenge 3-5-2

# https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv

# Let's build an interactive pivot table in streamlit!

# - create a row and column selection widgets allowing the user to select one of the following columns:  
# `'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
# - create a measure column selestion widget which allows the user to select one of these columns:  
# `'Completion_Time','Student_Score'`
# - build the pivot table dataframe from the inputs. use the average for the `aggfunc`
# - display the pivot table!

# **EXTRA CHALLENGE:** Do not allow the name value in row and column!
import pandas as pd
import streamlit as st

url = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'
df = pd.read_csv(url)
selections = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
row_selection = st.selectbox('Select a row:', selections)
if row_selection in selections:
    selections.remove(row_selection)
columns_selection = st.selectbox('Select a column:', selections)
measure_selection = st.selectbox('Select a measure:', ['Completion_Time','Student_Score'])
df_pivot = df.pivot_table(index=row_selection, columns=columns_selection, values=measure_selection, aggfunc='mean')
st.dataframe(df_pivot)