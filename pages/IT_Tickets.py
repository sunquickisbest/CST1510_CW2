import streamlit as st
import sqlite3 as sql
import plotly.express as px
import pandas as pd

with sql.connect("project_data.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM IT_Tickets")
    Tickets = pd.read_sql_query("SELECT * FROM IT_Tickets", connection)
    PriorityOverCount = Tickets.value_counts("priority").reset_index()
    st.plotly_chart(px.bar(PriorityOverCount, x="priority", y="count" ,color="priority" ,color_discrete_map={"Low" : "#A5CF83", "Medium" : "#ECB65F", "High" : "#D51C39", "Critical" : "#760031"},category_orders={"priority": ["Low", "Medium", "High", "Critical"]}, title="Amount of tickets by type"))
    TicketsByStatus = Tickets.value_counts("status").reset_index()
    st.plotly_chart(px.bar(TicketsByStatus, x="status", y="count", color="status", color_discrete_map={"Open" : "#FB4141", "Resolved" : "#B0CE88", "In Progress" : "#F5C857", "Waiting for User" : "#FFFFF0"}, title="Tickets by status", category_orders={"status": ["Open", "In Progress", "Resolved", "Waiting for User"]}))
    st.dataframe(pd.read_sql("SELECT * FROM IT_Tickets", connection), hide_index=True)