import sqlite3 as sql
import pandas as pd

def CSVToDB(x, name):
    pd.read_csv(x).to_sql(name, con=sql.connect("../DATA/project_data.db"))

CSVToDB("DATA/cyber_incidents.csv", "CyberIncidents")
CSVToDB("DATA/datasets_metadata.csv", "Metadata")
CSVToDB("DATA/it_tickets.csv", "IT_Tickets")