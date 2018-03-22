import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
names_crim=[]

main_url = "http://bombayhighcourt.nic.in/libweb/historicalcases/Historical_Cases_Of_Bombay_High_Court.html"
response=requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

letters=soup.find_all("small")
i=0
while (i < len(letters)):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_crim.append(s.strip())

del names_crim[0]
del names_crim[len(names_crim)-1]

l=[]
letters2=soup.find_all("a")
for i in letters2:
    st=i['href']
    if(st not in l):
        if(st[0]!="h"):
            l.append("http://bombayhighcourt.nic.in/libweb/historicalcases/"+st)
        else:
            l.append(st)


del l[len(l)-1]
del l[len(l)-1]
del l[len(l)-1]


links_crim=list(OrderedDict.fromkeys(l))
for i,j in zip(names_crim,links_crim):
    print(i,j)
