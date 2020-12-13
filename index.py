import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\DB\tasks.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Tasks')
   
for row in cursor.fetchall():
    print (row)
