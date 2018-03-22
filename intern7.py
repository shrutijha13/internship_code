import requests
from bs4 import BeautifulSoup

main_url = "http://bombayhighcourt.nic.in/libweb/Dictionaries/"
response=requests.get(main_url+"dict.html")
soup = BeautifulSoup(response.content, 'html.parser')

names_lawdict=[]
letters=soup.find_all("small")
i=7
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
    i=i+2
    if(s.strip()==""):
        continue
    else:
        names_lawdict.append(s.strip())
letters2=soup.find_all("a")

links_lawdict=[]

i=1
while(i<len(letters2)-4):
    st=letters2[i]['href']
    if(st[0]!="h"):
        links_lawdict.append(main_url+st)
    else:
        links_lawdict.append(st)
    i=i+2
k=1
for i,j in zip(names_lawdict,links_lawdict):
    print(k,i,j)
    k=k+1