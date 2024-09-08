import pandas as pd
import os
from db_connection import create_connection  

def expert_level(age):
    if age <= 30:
        return 'noob'
    elif age <=50:
        return 'mid'
    elif age > 50:
        return 'expert'
    
    return 'no label'

# Create the database connection using SQLAlchemy engine
engine = create_connection()

# SQL query to fetch the required data
query = "SELECT * FROM age_income;"  

# Read the data into a pandas DataFrame using SQLAlchemy connection
df = pd.read_sql(query, engine)

df['experience_level'] = df['Age'].apply(lambda x: expert_level(x))

print(df.head(10))
