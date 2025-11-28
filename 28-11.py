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

# 3. Insert some data
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Anna", 16, "10A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Luis", 17, "11B"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Marta", 15, "9C"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Pedro", 19, "9C"))

# Commit the changes
connection.commit()

# 4. Query the data
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("List of students:")
for student in students:
    print(student)

# 5. Close the connection
connection.close()
