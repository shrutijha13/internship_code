import requests

headers={'Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Host':'59.180.234.21:8080','Content-Length':'125'}
url = "http://59.180.234.21:8080/citizen/regfirsearchpage.htm"
payload='sdistrict=8162&spolicestation=8162001&firFromDateStr=&firToDateStr=&regFirNo=12&radioValue=undefined&searchName=&firYear=2017'
r = requests.post(url, headers=headers, params=payload)
s=r.json()

date=[]
record_created_on=[]
firNumDisp=[]
for i in s['list']:
    date.append(i['firRegDate'])
    record_created_on.append(i["recordCreatedOn"])
    firNumDisp.append(i["firNumDisplay"])

#print(s['list'][0])
print(date)
print(record_created_on)
print(firNumDisp)