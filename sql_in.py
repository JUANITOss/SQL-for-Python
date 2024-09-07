import pandas as pd
import os
from db_connection import create_connection  

# Create the database connection using SQLAlchemy engine
engine = create_connection()

# SQL query to fetch the required data
query = "SELECT * FROM age_income;"  

# Read the data into a pandas DataFrame using SQLAlchemy connection
df = pd.read_sql(query, engine)

# Declaring registers to look for
names = ['Gisela','Jordan','Hiroko']

print(df[df.Name.isin(names)])