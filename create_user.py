from app.database.db import get_db_connection
import bcrypt

username = "shop_staff"
password = "password123"

hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

conn = get_db_connection()
cursor = conn.cursor()

query = """
INSERT INTO users (
    username,
    password_hash,
    role
)
VALUES (%s, %s, %s)
"""

values = (
    username,
    hashed_password,
    'staff'
)

cursor.execute(query, values)
conn.commit()

cursor.close()
conn.close()

print("User created successfully!")