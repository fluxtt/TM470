# This cannot be run from the tests folder as it will cause circular imports. It is meant to be run from the root of the project to test the database connection.
from app.database.db import get_db_connection

try:
    conn = get_db_connection()
    
    if conn.is_connected():
        print("Database connection successful!")
        conn.close()
        
except Exception as e:
    print("Error:", e)