import sqlite3 as sql
import streamlit as st
import pandas as pd
import plotly.express as px
with sql.connect("DATA/project_data.db") as connection:
    cursor = connection.cursor()
    df = pd.read_sql_query("SELECT * FROM Metadata", connection)
    ### Make a pie chart by the amount of columns
    fig = px.pie(df, values='columns', title='Count of Tickets', names='name')
    ### Make the pie chart show the name
    fig.update_traces(textinfo='label')
    st.plotly_chart(fig)
    st.dataframe(df, hide_index=True)