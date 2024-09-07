# db_connection.py
from sqlalchemy import create_engine

def create_connection():
    """Creates and returns a SQLAlchemy engine to the database."""
    user = 'oscarval_user'
    password = 'learnsql123'
    host = 'oscarvalles.com'
    port = 3306
    database = 'oscarval_sql_course'

    engine_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    
    # Create and return the engine
    engine = create_engine(engine_url)
    return engine
