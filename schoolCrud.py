import sqlite3

# 1. Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# 2. Create tables
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
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               description TEXT,
               year INTEGER
               )""" )

# 3. Insert some data
#Student Data
#cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Anna", 16, "10A"))

#Teacher Data
#cursor.execute("INSERT INTO teachers (name, email, phone) VALUES (?, ?, ?)", ("Anna", "anna@gmail.com", "123456789"))

#Course Data
#cursor.execute("INSERT INTO courses (name, description, year) VALUES (?, ?, ?)", ("Mathematics", "Basic Math Course", 10))

# 4. Update and Delete data

# Update Student
#cursor.execute('UPDATE students SET name = "ID10" WHERE id = 10')

# Delete Student
#cursor.execute('DELETE FROM students WHERE id > 10')

# Update Teacher
#cursor.execute('UPDATE teachers SET name = "ID10" WHERE id = 10')

# Delete Teacher
# cursor.execute('DELETE FROM teachers WHERE id > 10')


# Update Course
#cursor.execute('UPDATE courses SET name = "ID10" WHERE id = 1')

# Delete Course
#cursor.execute('DELETE FROM courses WHERE id = 1')

# Commit the changes
connection.commit()

# 5. Read data
# Read Students
#cursor.execute("SELECT * FROM students")
#students = cursor.fetchall()
#print("List of students:")
#for teacher in students:
 #   print(student)

# Read Teachers
#cursor.execute("SELECT * FROM teachers")
#teachers = cursor.fetchall()
#print("List of teachers:")
#for teacher in teachers:
 #   print(teacher)

# Read Courses 
cursor.execute("SELECT * FROM courses")
courses = cursor.fetchall()
print("List of courses:")
for course in courses:
    print(course)



# 6. Close the connection
connection.close()