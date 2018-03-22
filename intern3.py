import requests
from bs4 import BeautifulSoup
names_a=[]
links_a=[]
main_url="http://bombayhighcourt.nic.in/libweb/acts/"
try:
    url=main_url+"listofmahacts.html"
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')

except Exception as e:
    print(str(e))

letters=soup.find_all("small")
letters_two=soup.find_all("td",style="vertical-align: top; width: 848px;")

i = 0

while (i < len(letters)):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    #print(letters_new)
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
    elif(s.strip()[0]=="0" or s.strip()[0]=="1" or s.strip()[0]=="2" or s.strip()[0]=="3"):
        continue
    else:
        names_a.append(s.strip())
del names_a[0]
del names_a[len(names_a)-1]

for i in names_a:
    if (len(i)==1):
        names_a.remove(i)
k = 0
while (k < 7):
    del names_a[339]
    k = k + 1

for link in letters_two:
    st=link.find("a",style="text-decoration: none;")
    if(link.get_text()==None or len(link.get_text())==1):
        continue
    else:
        if(st==None):
            links_a.append(None)
        else:
            st=st['href']
            links_a.append(st)

links_a.insert(22,"Stateact/2014acts/2014.29.pdf")
links_a.insert(28,"1947.34.pdf")
links_a.insert(38,"1944.02.pdf")
links_a.insert(144,"1866.23.pdf")
links_a.insert(145,"1955.55.pdf")
links_a.insert(338,"2001.23.pdf")
links_a.insert(353,"1853.11.pdf")
links_a.insert(381,"2004.08.PDF")

real_links_a=[]
for s in links_a:
    if(s==None):
        real_links_a.append(None)
    else:
        if(s[0]=="h"):
            real_links_a.append(s)
        else:
            real_links_a.append(main_url+s)
