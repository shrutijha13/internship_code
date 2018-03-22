# Importing necessary modules
from bs4 import BeautifulSoup
import urllib3
import requests

names=[]
links=[]
# Basic python code for parsing html
main_url = "http://bombayhighcourt.nic.in/libweb/rulec/"
response = requests.get(main_url+"centralrules.html")
soup = BeautifulSoup(response.content, 'html.parser')
# soup1=soup.prettify()

letters = soup.find_all("li")
i = 0
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
    names.append(s.strip())

for link in letters:
    st=link.find("a")
    if(st==None):
        links.append(None)
        continue
    else:
        st=st['href']
        links.append(st)


real_links=[]
del links[90]
links.insert(90,None)

del links[252]
links.insert(252,None)

del links[130]
links.insert(130,None)

del links[180]
links.insert(180,None)

del links[318]
links.insert(318,None)

for s in links:
    if(s==None):
        real_links.append(None)
    else:
        if(s[0]=="h"):
            real_links.append(s)
        else:
            real_links.append(main_url+s)
k=1
for i,j in zip(names,real_links):
    print(k,i,"      ",j)
    k=k+1