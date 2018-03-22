import pymysql
from intern8 import names_fc,links_fc,names_sc,links_sc,names_tc,links_tc, names_foc,links_foc,names_fifc,links_fifc;
from intern8 import names_sixc,links_sixc,names_sevc,links_sevc,names_eigc,links_eigc,names_ninc,links_ninc,names_tenc,links_tenc;
from intern8 import names_elec,links_elec,names_twc,links_twc,names_thc,links_thc,names_fourc,links_fourc,names_fiftc,links_fiftc;
from intern8 import names_sixtc,links_sixtc,names_sevtc,links_sevtc,names_eigtc,links_eigtc,names_nintc,links_nintc,names_twenc,links_twenc;

connection=pymysql.connect(host='dhcapi.chneyatcrvgc.us-east-2.rds.amazonaws.com',use_unicode=True,db='bombay_high_court_info',user='root',port=3306,password='lawfacto',charset='utf8')
cursor=connection.cursor()

cursor.execute("CREATE TABLE FIRST_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_fc)):
    k=i+1
    cursor.execute("INSERT INTO FIRST_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_fc[i],links_fc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE SECOND_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_sc)):
    k=i+1
    cursor.execute("INSERT INTO SECOND_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_sc[i],links_sc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE THIRD_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_tc)):
    k=i+1
    cursor.execute("INSERT INTO THIRD_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_tc[i],links_tc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE FOURTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_foc)):
    k=i+1
    cursor.execute("INSERT INTO FOURTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_foc[i],links_foc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE FIFTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_fifc)):
    k=i+1
    cursor.execute("INSERT INTO FIFTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_fifc[i],links_fifc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE SIXTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_sixc)):
    k=i+1
    cursor.execute("INSERT INTO SIXTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_sixc[i],links_sixc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE SEVENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_sevc)):
    k=i+1
    cursor.execute("INSERT INTO SEVENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_sevc[i],links_sevc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE EIGHTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_eigc)):
    k=i+1
    cursor.execute("INSERT INTO EIGHTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_eigc[i],links_eigc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE NINTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_ninc)):
    k=i+1
    cursor.execute("INSERT INTO NINTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_ninc[i],links_ninc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE TENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_tenc)):
    k=i+1
    cursor.execute("INSERT INTO TENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_tenc[i],links_tenc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE ELEVENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_elec)):
    k=i+1
    cursor.execute("INSERT INTO ELEVENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_elec[i],links_elec[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE TWELFTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_twc)):
    k=i+1
    cursor.execute("INSERT INTO TWELFTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_twc[i],links_twc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE THIRTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_thc)):
    k=i+1
    cursor.execute("INSERT INTO THIRTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_thc[i],links_thc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE FOURTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_fourc)):
    k=i+1
    cursor.execute("INSERT INTO FOURTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_fourc[i],links_fourc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE FIFTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_fiftc)):
    k=i+1
    cursor.execute("INSERT INTO FIFTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_fiftc[i],links_fiftc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE SIXTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_sixtc)):
    k=i+1
    cursor.execute("INSERT INTO SIXTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_sixtc[i],links_sixtc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE SEVENTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_sevtc)):
    k=i+1
    cursor.execute("INSERT INTO SEVENTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_sevtc[i],links_sevtc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE EIGHTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_eigtc)):
    k=i+1
    cursor.execute("INSERT INTO EIGHTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_eigtc[i],links_eigtc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE NINTEENTH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_nintc)):
    k=i+1
    cursor.execute("INSERT INTO NINTEENTH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_nintc[i],links_nintc[i]))
    i=i+1
connection.commit()

cursor.execute("CREATE TABLE TWENTIETH_COMMISSION(ID INT PRIMARY KEY NOT NULL,RULES TEXT, URLS TEXT);")
i=0
while(i<len(names_twenc)):
    k=i+1
    cursor.execute("INSERT INTO TWENTIETH_COMMISSION(ID,RULES,URLS) VALUES(%s,%s,%s)",(k,names_twenc[i],links_twenc[i]))
    i=i+1
connection.commit()

connection.close()

print("Successful")
