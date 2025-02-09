from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to get a database connection
def get_db():
    conn = sqlite3.connect('scraped_data.db')  # Path to your SQLite database file
    return conn, conn.cursor()

@app.route('/')
def read_root():
    return jsonify({"message": "Welcome to the Flask application!"})

@app.route('/machine-learning-finance', methods=['GET'])
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
        return jsonify({"data": data})
        
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)})

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    conn, cursor = get_db()
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "username": user[0],  # Assuming username is the first column
            "password": user[1]   # Assuming password is the second column
        })
        
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)})

@app.route('/signup/', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    conn, cursor = get_db()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        
        return jsonify({"message": f"User {username} created successfully!"})
        
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
