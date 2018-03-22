import urllib
from bs4 import BeautifulSoup
import mechanize

url="http://59.180.234.21:8080/citizen/firSearch.htm"
br=mechanize.Browser(factory=mechanize.RobustFactory())
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
br.addheaders.append( ['Accept-Encoding','gzip'] )
br.open(url)
response=br.response()

'''br.select_form(nr=0)
br[id='districtId']="NEW DELHI"
br["policeStationId"]="CONNAUGHT PLACE"
br["firYear"]="2017"
br["regFirNo"]="12"
response=br.submit()
content=response.read()
print content
'''
br.select_form("citizenfaqForm")
br.form['districtId']="NEW DELHI"
br.form["policeStationId"]="CONNAUGHT PLACE"
br.form["firYear"]="2017"
br.form["regFirNo"]="12"

br.submit()