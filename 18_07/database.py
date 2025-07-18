import mysql.connector as mysql

db = mysql.connect(
    user="root",
    passwd="admin",
    host="localhost",
    port=3306,
    database="testdb"
)


cursor = db.cursor(dictionary=True)
# cursor.execute("SELECT * FROM STUDENTS")
# data = cursor.fetchall() #Unknown amount of results
#
# print(data)
#
# for student in data:
#     print(student["second_name"])

# cursor.execute("SELECT * FROM students WHERE id = 2")
# data = cursor.fetchone() #Only one result
# print(data)

# query = "SELECT * FROM students WHERE name = %s and second_name = %s"
# cursor.execute(query, (input('name '), input('second_name ')))
# #cursor.execute(query, ('Bogdan', 'Bondarenko'))
# print(cursor.fetchall())

#cursor.execute("INSERT INTO STUDENTS (name, second_name, group_id) VALUES ('Ivan', 'Ivanov', 2 )")
# cursor.execute("INSERT INTO STUDENTS (name, second_name, group_id) VALUES ('Andrey', 'Petrov', 1 )")
# cursor.execute("INSERT INTO STUDENTS (name, second_name, group_id) VALUES ('Vova', 'Lagotiuk', 2 )")
#last_id = cursor.lastrowid
#ursor.execute(f"SELECT * FROM students WHERE id = {last_id}")
select_query = '''
    SELECT * FROM students 
    WHERE name = 'George' 
    AND second_name = 'Washington' 
'''
cursor.execute(select_query)
print(cursor.fetchone())



db.commit()



db.close()
