# Importing necessary modules
#import urllib.request
#import urllib.parse
import requests
from bs4 import BeautifulSoup
names_m=[]
links_m=[]
main_url="http://bombayhighcourt.nic.in/libweb/rules/"
try:
    url=main_url+"MaharashtraRules.html"
    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    #req = urllib.request.Request(url, headers = headers)
    #resp = urllib.request.urlopen(req)
    #respData = resp.read()
    # saveFile = open('withHeaders.txt','w')
    # saveFile.write(str(respData))
    # saveFile.close()
    # print(respData)
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')

except Exception as e:
    print(str(e))

letters=soup.find_all("small")
letters_two=soup.find_all("tr")
#print(letters_two)
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
    if(s.strip()==""):
        continue
    else:
        names_m.append(s.strip())
del names_m[len(names_m)-1]
#print(len(names_m))

for link in letters_two:
    st=link.find("a")
    if(st==None):
        continue
    else:
        st=st['href']
        links_m.append(st)

del links_m[len(links_m)-1]
del links_m[len(links_m)-1]
del links_m[len(links_m)-1]
links_m.append("SociRegistrationMahrules1971.pdf")

real_links_m=[]
for s in links_m:
    if(s==None):
        real_links_m.append(None)
    else:
        if(s[0]=="h"):
            real_links_m.append(s)
        else:
            real_links_m.append(main_url+s)
