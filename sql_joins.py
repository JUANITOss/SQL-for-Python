import pandas as pd
import os
from db_connection import create_connection  

# Create the database connection using SQLAlchemy engine
engine = create_connection()

# SQL query to fetch the required data
age_income = "SELECT * FROM age_income;"  
name_children = "SELECT * FROM name_children;"

# Read the data into a pandas DataFrame using SQLAlchemy connection
df1 = pd.read_sql(age_income, engine)
df2 = pd.read_sql(name_children, engine)

query = pd.merge(df1, df2, how='inner', left_on='Name', right_on='Name') # can be left, right, outer, inner 

print(query)