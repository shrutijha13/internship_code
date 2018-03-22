import requests
from bs4 import BeautifulSoup

main_url = "http://bombayhighcourt.nic.in/libweb/reglc/"
response=requests.get(main_url+"regulcindex.html")
soup = BeautifulSoup(response.content, 'html.parser')

names_creg=[]
links_creg=[]
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
        names_creg.append(s.strip())

for link in letters:
    st=link.find("a")
    if(st==None):
        continue
    else:
        st=st['href']
        if(st[0]!="h"):
            links_creg.append(main_url+st)
        else:
            links_creg.append(st)

