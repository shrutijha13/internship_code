from intern1 import real_links, names
from intern2 import real_links_m, names_m
from intern3 import real_links_a, names_a

import pymysql
connection=pymysql.connect(host='dhcapi.chneyatcrvgc.us-east-2.rds.amazonaws.com',use_unicode=True,db='bombay_high_court_info',user='root',port=3306,password='lawfacto',charset='utf8')
cursor=connection.cursor()

cursor.execute("DROP TABLE CENTRAL_LEGISLATION_RULES")
cursor.execute("CREATE TABLE CENTRAL_LEGISLATION_RULES(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")

i=0
while(i<len(names)):
    k=i+1
    cursor.execute("INSERT INTO CENTRAL_LEGISLATION_RULES(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names[i],real_links[i]))
    i=i+1
connection.commit()


cursor.execute("CREATE TABLE STATE_LEGISLATION_RULES(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_m)):
    k=i+1
    cursor.execute("INSERT INTO STATE_LEGISLATION_RULES(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_m[i],real_links_m[i]))
    i=i+1
connection.commit()


cursor.execute("CREATE TABLE STATE_LEGISLATION_ACTS(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_a)):
    k=i+1
    cursor.execute("INSERT INTO STATE_LEGISLATION_ACTS(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_a[i],real_links_a[i]))
    i=i+1
connection.commit()

connection.close()

print("Successful")