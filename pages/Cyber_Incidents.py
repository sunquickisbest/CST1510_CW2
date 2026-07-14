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

    st.write("Click on the Severity to filter")

    SeverityAndCategory = pd.crosstab(Severity, Category, colnames=["Category"], rownames=["Severity"])
    SeverityAndCategory = SeverityAndCategory.reindex(["Low", "Medium", "High", "Critical"])
    st.plotly_chart(px.bar(SeverityAndCategory, color="Category", color_discrete_map={"Misconfiguration":"#EED9B9", "Phishing":"#D53E0F", "DDoS":"#9B0F06", "Unauthorized Access":"#5E0006", "Malware" : "#D62828"}))
    st.markdown("""<p style="position: relative; text-align:right; left: 10px; bottom: 280px;"> Click on the Category to filter </p>""", unsafe_allow_html=True)
    st.dataframe(pd.read_sql("SELECT * FROM CyberIncidents", connection), hide_index=True)


    with st.form("Add Incident"):
        severitySelected = st.selectbox("Select the severity", ("Critical", "High", "Medium", "Low"))
        categorySelected = st.selectbox("Select the category", ("Malware", "Misconfiguration", "Phishing", "DDoS", "Unauthorized Access"))
        status = st.selectbox("Select the status", ("Open", "In Progress", "Resolved", "Closed"))
        date = st.datetime_input("Choose the Date")
        if st.form_submit_button("Add Incident", key="addIncidentButton"):
            cursor.execute("INSERT INTO CyberIncidents(incident_id, timestamp, severity, category, status, description) VALUES (?,?,?,?,?,?)", (max(IncidentIDs)+1, date, severitySelected, categorySelected, status, f"Incident {((max(IncidentIDs)+1)-1000)} description"))
            connection.commit()
            st.rerun()


    st.html("""<style> 
    
            .st-emotion-cache-4cktc5 p {
                text-align: right;
                position: relative;
                bottom: 300px;
                left: 60px;
                font-size: 13px;
            }
            
            
            </style>""")