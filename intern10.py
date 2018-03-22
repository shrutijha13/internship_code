import requests
from bs4 import BeautifulSoup

main_url = "http://bombayhighcourt.nic.in/libweb/regls/"
response=requests.get(main_url+"regulsindex.html")
soup = BeautifulSoup(response.content, 'html.parser')

names_sreg=[]
links_sreg=[]

letters=soup.find_all("li")
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
        names_sreg.append(s.strip())

for link in letters:
    st=link.find("a")
    if(st==None):
        continue
    else:
        st=st['href']
        if(st[0]!="h"):
            links_sreg.append(main_url+st)
        else:
            links_sreg.append(st)

for i,j in zip(names_sreg,links_sreg):
    print(i,j)