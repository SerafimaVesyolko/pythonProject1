import sqlite3

cconnection = sqlite3.Connection('sqlite3.db')
cursor = cconnection.cursor()

cursor.execute('create table Table1 ( first,second,third )')
cursor.execute('create table Table2 ( first,second,third, fourth,fifth)')
cursor.execute('insert into Table1(first ,second, third ) values ("one","two", "three")')
cursor.execute('insert into Table2(third , fourth , fifth ) values (3,4, 5)')
cconnection.commit()
cursor.close()

