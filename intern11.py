import  pymysql
from intern6 import names_crim,links_crim
from intern7 import names_lawdict,links_lawdict
from intern9 import names_creg,links_creg
from intern10 import names_sreg,links_sreg

connection=pymysql.connect(host='dhcapi.chneyatcrvgc.us-east-2.rds.amazonaws.com',use_unicode=True,db='bombay_high_court_info',user='root',port=3306,password='lawfacto',charset='utf8')
cursor=connection.cursor()
#cursor.execute("DROP TABLE CASES_OF_BOMBAY")
cursor.execute("DROP TABLE CENTRAL_LEGISLATION_REGULATIONS")
cursor.execute("DROP TABLE STATE_LEGISLATION_REGULATIONS")

cursor.execute("CREATE TABLE CENTRAL_LEGISLATION_REGULATIONS(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_creg)):
    k=i+1
    cursor.execute("INSERT INTO CENTRAL_LEGISLATION_REGULATIONS(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_creg[i],links_creg[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE STATE_LEGISLATION_REGULATIONS(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_sreg)):
    k=i+1
    cursor.execute("INSERT INTO STATE_LEGISLATION_REGULATIONS(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_sreg[i],links_sreg[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE CASES_OF_BOMBAY(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_crim)):
    k=i+1
    cursor.execute("INSERT INTO CASES_OF_BOMBAY(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_crim[i],links_crim[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE LAW_DICTIONARIES(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_lawdict)):
    k=i+1
    cursor.execute("INSERT INTO LAW_DICTIONARIES(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_lawdict[i],links_lawdict[i]))
    i=i+1
connection.commit()

connection.close()

print("Successful")