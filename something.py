from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/Users/shrutijha/Downloads/pyChrome/bin/chromedriver",chrome_options=chrome_options)  # Optional argument, if not specified will search path.

main_date=time.strptime("01/07/2015","%d/%m/%Y")

y=raw_input("Enter year:")
fno=raw_input("Enter FIR No.:")
date_from=raw_input("Enter date from:")
date_to=raw_input("Enter date to:")
entered_date=time.strptime(date_from,"%d/%m/%Y")

if(entered_date>main_date):
    driver.get('http://59.180.234.21:8080/citizen/firSearch.htm')
else:
    driver.get("http://59.180.234.21:85/index.aspx")

dis=raw_input("Enter district:")
ps=raw_input("Enter police station:")
district=Select(driver.find_element_by_id("sdistrict"))
time.sleep(1)
district.select_by_visible_text(dis)

year=Select(driver.find_element_by_id("firYear"))
year.select_by_visible_text(y)

policest=Select(driver.find_element_by_id("spolicestation"))
time.sleep(1)
policest.select_by_visible_text(ps)

search_box1 = driver.find_element_by_id("regFirNo")
search_box1.send_keys(fno)

date1=driver.find_element_by_id("datetimer8")
date1.send_keys(date_from)

date2=driver.find_element_by_id("datetimer9")
date2.send_keys(date_to)

driver.find_element_by_id("searchButton ").click()

#b="https://docs.google.com/viewer?url=http://59.180.234.21:8080/citizen/gefirprint.htm?firRegNo=8165011170212&stov=89SE-19KA-BIEX-D22B-FY0Z-TG1J-FMMD-ETA1"
#driver.execute_script("window.open('https://docs.google.com/viewer?url=http://59.180.234.21:8080/citizen/gefirprint.htm?firRegNo=8165011170212&stov=89SE-19KA-BIEX-D22B-FY0Z-TG1J-FMMD-ETA1', 'new_window')")


WebDriverWait(driver, timeout=10).until(
         lambda x: x.find_element_by_id("0"))

html_page=driver.page_source
soup=BeautifulSoup(html_page,"html.parser")
driver.close()
letters=[]
info=[]
link=[]
i=0
while(True):
    letters=soup.find_all("tr",id=str(i))
    i=i+1
    if letters==[]:
        break
    for k in letters:
        info.append(str(k.get_text()))
        link.append(str(k.find("a")["href"]))

i=0
print "SNo.  FIR No.  FIR Date  FIR Year"
while(i<len(info)):
    print info[i]
    i=i+1

choice=int(input("Which do you want to open? :"))
ch=0

for i in info:
    ch=ch+1
    if(ch==choice):
        driver=webdriver.Chrome("/Users/shrutijha/Downloads/pyChrome/bin/chromedriver")
        driver.get("https://docs.google.com/viewer?url=http://59.180.234.21:8080"+link[ch-1])

