from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select

# 1. Setup the Database Connection
# Using SQLite for simplicity (replace with your DB URL if needed)
engine = create_engine('sqlite:///my_database.db', echo=True)
conn = engine.connect()
metadata = MetaData()

# 2. Define a Table Schema
# Creating a 'users' table with SQLAlchemy
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer),
              Column('email', String))

# Create the table if it doesn't exist
metadata.create_all(engine)

# 3. CRUD Operations
# CREATE (Insert Data)
def insert_user(name, age, email):
    insert_query = users.insert().values(name=name, age=age, email=email)
    conn.execute(insert_query)

# READ (Select Data)
def get_users():
    select_query = select([users])
    result = conn.execute(select_query)
    for row in result:
        print(row)

# UPDATE (Update Data)
def update_user_email(name, new_email):
    update_query = users.update().where(users.c.name == name).values(email=new_email)
    conn.execute(update_query)

# DELETE (Delete Data)
def delete_user(name):
    delete_query = users.delete().where(users.c.name == name)
    conn.execute(delete_query)

# 4. Example Usage of CRUD Functions
if __name__ == "__main__":
    # Insert Users
    insert_user("John Doe", 30, "john@example.com")
    insert_user("Jane Doe", 25, "jane@example.com")
    
    # Read Users
    print("Current Users:")
    get_users()

    # Update a User's Email
    update_user_email("John Doe", "john_doe@example.com")

    # Read Users Again
    print("\nUsers After Update:")
    get_users()

    # Delete a User
    delete_user("Jane Doe")

    # Read Users After Deletion
    print("\nUsers After Deletion:")
    get_users()

# 5. Close the Connection
conn.close()
