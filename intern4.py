from intern6 import names_crim,links_crim
import sqlite3

conn=sqlite3.connect("test.db")

cursor=conn.cursor()
#cursor.execute('''DROP TABLE CENTRAL_LEGISLATION_RULES''')
cursor.execute('''CREATE TABLE CASES_OF_BOMBAY
(ID INT PRIMARY KEY NOT NULL,
RULES TEXT,
URLS TEXT);''')

i=0
while(i<len(names_crim)):
    k=i+1
    cursor.execute('''INSERT INTO CASES_OF_BOMBAY(ID,RULES,URLS)
    VALUES(?,?,?)''',(k,names_crim[i],links_crim[i]))
    i=i+1
conn.commit()
cursor.execute('''SELECT ID,RULES,URLS FROM CASES_OF_BOMBAY''')
all_rows=cursor.fetchall()
for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0],row[1],row[2]))
print("Successful")
