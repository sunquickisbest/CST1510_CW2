import sqlite3 as sql
import streamlit as st
import pandas as pd
import plotly.express as px
with sql.connect("project_data.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CyberIncidents")
    Data = cursor.fetchall()
    IncidentIDs = []
    Timestamps = []
    Severity = []
    Category = []
    for i in Data:
        IncidentIDs.append(i[1])
        Timestamps.append(i[2].split(" "))
        Severity.append(i[3])
        Category.append(i[4])
    Date = []
    Time = []
    for i in Timestamps:
        Date.append(i[0])
        Time.append(i[1])
    IncidentsOverTime = {"Incident ID" : IncidentIDs, "Date" : Date, "Severity" : Severity, "Category" : Category}
    df = pd.DataFrame(IncidentsOverTime)
    generalInfo = px.scatter(df, x="Date", y="Incident ID", hover_data=["Incident ID", "Date", "Severity", "Category"],
    color="Severity",color_discrete_map={"Critical":"Red", "High": "Red", "Medium" : "Orange", "Low": "Gray"})
    generalInfo.update_traces(marker={"size": 12.5})
    st.plotly_chart(generalInfo)
    SeverityAndCategory = pd.crosstab(Severity, Category, colnames=["Category"], rownames=["Severity"])
    st.plotly_chart(px.bar(SeverityAndCategory, color="Category", color_discrete_map={"Misconfiguration":"Gray", "Phishing":"Orange", "DDoS":"Red", "Unauthorized Access":"Brown"}))