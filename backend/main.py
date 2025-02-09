from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# CORS configuration to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Function to get a database connection
def get_db():
    conn = sqlite3.connect('scraped_data.db')  # Path to your SQLite database file
    return conn, conn.cursor()

@app.get("/machine-learning-finance")
def get_machine_learning_finance():
    conn, cursor = get_db()
    try:
        cursor.execute("SELECT * FROM machine_learning_finance")  # Adjust table name as needed
        rows = cursor.fetchall()
        
        data = [
            {   
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "createdat": row[3],
                "topic": row[4]
            }
            for row in rows
        ]
        
        conn.close()
        return {"data": data}
        
    except Exception as e:
        conn.close()
        return {"error": str(e)}

# Endpoint to get a single user by username
@app.get("/user/{username}")
def get_user(username: str):
    conn, cursor = get_db()
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "username": user[0],  # Assuming username is the first column
            "password": user[1]   # Assuming password is the second column
        }
        
    except Exception as e:
        conn.close()
        return {"error": str(e)}

# Endpoint to create a new user (POST request)
@app.post("/user/")
def create_user(username: str, password: str):
    conn, cursor = get_db()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

        return {"message": f"User {username} created successfully!"}
        
    except Exception as e:
        conn.close()
        return {"error": str(e)}

