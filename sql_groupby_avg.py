import pandas as pd
import os
from db_connection import create_connection  

# Create the database connection using SQLAlchemy engine
engine = create_connection()

# SQL query to fetch the required data
query = "SELECT * FROM age_income;"  

# Read the data into a pandas DataFrame using SQLAlchemy connection
df = pd.read_sql(query, engine)

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Group by 'Marital Status' and compute the mean for numeric columns
query = numeric_df.groupby(df['Marital Status'], dropna=False).mean()

print(query)
