from bs4 import BeautifulSoup
import requests

r = requests.get(url ='https://www.change.org/p/free-nazanin-ratcliffe?source_location=discover_feed')

data = r.text

soup = BeautifulSoup(data, 'lxml')

title = soup.find('h1', {'class':'mtl mbxxxl xs-mts xs-mbxs petition-title'}).text

print(title)

a =soup.find('strong',{'class' : 'type-s type-weak'})

b = a.find_all('a')

starter_name = b[0].text

to_name = b[1].text

print(starter_name)
print(to_name)

desc = soup.find('div',{'class': 'rte js-description-content'}).text
print(desc)
