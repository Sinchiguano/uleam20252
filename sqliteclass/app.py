import sqlite3

#CREATE AND CONNECT TO A DATABASE CALLED SQLITE

conn=sqlite3.connect('studentsuleam.db')


cursor=conn.execute('''CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER) ''')


print('STUDENTS DATABASE WAS CREATED SUCCESSFULLY OR ALREADY CREATED')

conn.commit()


studentsList=[('juan',34),('pedro',23),('lucas',56)]

for name, age in studentsList:
    print(name)
    print(age)
    cursor.execute('INSERT INTO students (name,age) VALUES (?,?)',(name,age))
    conn.commit()
print('Everything is working fine .....')



cursor.execute('SELECT * FROM students ')

for row in cursor.fetchall():
    print(f'Id: {row[0]}, Name: {row[1]}, Age: {row[2]}')
    
conn.commit() 
conn.close()