import sqlite3 as sql
import streamlit as st
import pandas as pd
with sql.connect("project_data.db") as connection:
    cursor = connection.cursor()
    df = pd.read_sql_query("SELECT * FROM Metadata", connection)
    st.dataframe(df)