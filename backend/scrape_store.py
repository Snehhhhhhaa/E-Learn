import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Step 1: Connect to SQLite database
conn = sqlite3.connect('scraped_data.db')
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS machine_learning_finance")

# Ensure the table exists with the correct columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS machine_learning_finance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    example_title TEXT NOT NULL,
    example_description TEXT,
    createdat TEXT,
    topic TEXT
)
''')

# Step 2: Scrape data from the provided URL
url = 'https://builtin.com/artificial-intelligence/machine-learning-finance-examples'
response = requests.get(url)

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find the relevant data you want to extract
examples = soup.find_all('h2')  # Adjust the tag as needed

# Step 5: Loop through the examples and extract title, description, and topic
for example in examples:
    title = example.get_text(strip=True)  # Extract title
    description = example.find_next('p')  # Find the next paragraph for description
    description_text = description.get_text(strip=True) if description else "No description available."
    topic_tag = example.find_next('span', class_='topic-class')  # Adjust class if needed
    topic = None

    # Get current date and day
    createdat = datetime.now().strftime("%Y-%m-%d (%A)")  # Example: "2025-02-08 (Saturday)"

    # Insert the extracted data into the database
    cursor.execute("""
        INSERT INTO machine_learning_finance (example_title, example_description, createdat, topic) 
        VALUES (?, ?, ?, ?)
    """, (title, description_text, createdat, "ml"))
    
    cursor.execute("UPDATE machine_learning_finance SET topic = ? WHERE topic IS NULL", ("ml",))  
# Step 6: Commit changes and close the connection
conn.commit()
conn.close()

print("Data scraped, inserted successfully, and table recreated!")

