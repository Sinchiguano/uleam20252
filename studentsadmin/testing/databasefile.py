import sqlite3

#CREATE AND CONNECT TO A DATABASE
conn=sqlite3.connect('myfirstdatabase.db')
#CREATE A CURSOR TO EXECUTE SQL STATEMENTS
cursor=conn.cursor()

#CREATE A TABLE 
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER)''')

print('STUDENTS TABLE CREATED OR ALREADY EXISTS')

# SAVE AND CLOSE
conn.commit()
# conn.close()

studentsList=[('cesar',10),('carlos',35),('pepe',45)]


for name, age in studentsList:
    print(name)
    print(age)
    cursor.execute('INSERT INTO students (name, age) VALUES (?,?)',(name,age))
    conn.commit()

# QUERY THE TABLE TO VERIFY THE INSERTED DATA
cursor.execute('SELECT * FROM  students')

for row in cursor.fetchall():
    print(f"ID {row[0]} NAME {row[1]} AGE {row[2]}")

conn.commit()

cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('cesar', 10))
cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('carlos', 35))
cursor.execute('SELECT * FROM students')
print(cursor.fetchall())  # Shows [(1, 'cesar', 10), (2, 'carlos', 35)]
cursor.execute('DELETE FROM students WHERE id = 1')
cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('pepe', 45))
cursor.execute('SELECT * FROM students')
print(cursor.fetchall())  # Might show [(2, 'carlos', 35), (1, 'pepe', 45)] without AUTOINCREMENT

conn.close()
