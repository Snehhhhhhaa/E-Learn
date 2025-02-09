import sqlite3
# Step 1: Connect to SQLite database
conn = sqlite3.connect('scraped_data.db')
cursor = conn.cursor()


# Ensure the table exists with the correct columns
cursor.execute('''
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)

''')

conn.commit()
conn.close()


