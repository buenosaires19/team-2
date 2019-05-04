import sqlite3
conn = sqlite3.connect('sqlite3.db')

c = conn.cursor()

# Create table USER
c.execute('''CREATE TABLE user
             (user_name text NOT NULL UNIQUE, password text NOT NULL, name text, birthdate text, school text, school_year, city text, province text, email text, user_id INTEGER PRIMARY KEY AUTOINCREMENT)''')
# Save (commit) the changes
conn.commit()
