import pandas as pd
import os
from db_connection import create_connection  

# Create the database connection using SQLAlchemy engine
engine = create_connection()

# SQL query to fetch the required data
query = "SELECT * FROM age_income;"  

# Read the data into a pandas DataFrame using SQLAlchemy connection
df = pd.read_sql(query, engine)

# Define the directory and filename to save the data
directory = os.path.join(os.getcwd(), 'csvs')  
filename = os.path.join(directory, 'age_income_table.csv')

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df.to_csv(filename, index=False)

# Now load the CSV file to process (if needed)
df = pd.read_csv(filename)

# Proceed with your data processing (if any)
print(df.head(10))  # Show the first few rows of the DataFrame
