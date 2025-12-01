import sqlite3

# 1. Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# 2. Create a table for students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone INTEGER
)
""")

# 3. Insert some data
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Anna", 16, "10A"))
cursor.execute('UPDATE students SET name = "ID10" WHERE id = 10')

cursor.execute("INSERT INTO teachers (name, email, phone) VALUES (?, ?, ?)", ("Anna", "anna@gmail.com", "123456789"))
cursor.execute('UPDATE teachers SET phone = "1001" WHERE id = 10')
cursor.execute('DELETE FROM teachers WHERE id > 10')

# Commit the changes
connection.commit()

# 4. Query the data
cursor.execute("SELECT * FROM teachers")
teachers = cursor.fetchall()

print("List of teachers:")
for teacher in teachers:
    print(teacher)

# 5. Close the connection
connection.close()