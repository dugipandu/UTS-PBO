import sqlite3

# Create a connection and cursor
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# Insert data
cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', ('john_doe', 'john@example.com'))

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Commit changes and close connection
conn.commit()
conn.close()
