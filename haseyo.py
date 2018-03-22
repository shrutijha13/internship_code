from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pytesseract

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/Users/shrutijha/Downloads/pyChrome/bin/chromedriver",chrome_options=chrome_options)
driver.get('http://59.180.234.21:85/index.aspx')

district_n=raw_input("Enter district:")
district_name=Select(driver.find_element_by_id("ddlDistrict"))
sleep(2)
district_name.select_by_visible_text(district_n)

policestn_n=raw_input("Enter police station:")
policestn_name=Select(driver.find_element_by_id("ddlPS"))
sleep(2)
policestn_name.select_by_visible_text(policestn_n)

y=raw_input("Enter year:")
year=Select(driver.find_element_by_id("ddlYear"))
sleep(2)
year.select_by_visible_text(y)

fno=raw_input("Enter FIR No.:")
search_box1 = driver.find_element_by_id("txtRegNo")
sleep(2)
search_box1.send_keys(fno)

driver.find_element_by_id("btnSearch").click()
sleep(2)

html_page=driver.page_source
soup=BeautifulSoup(html_page,"html.parser")

letters=soup.find_all("tr",attrs={'class': 'DataItemStyle '})
letters1=soup.find_all("tr",attrs={'class':'DataAlternateItemStyle '})

records=[]

k=1
if letters==[]:
    print("No record exists")
else:
    for i in letters:
        letters_no=i.find_all("td")
        recs=[]
        recs.append(k)
        for i in letters_no:
            recs.append(i.text)
        del recs[-1]
        k=k+2
    records.append(recs)

k=2
if letters1==[]:
    pass
else:
    for i in letters1:
        letters1_no=i.find_all("td")
        recs=[]
        recs.append(k)
        for i in letters1_no:
            recs.append(i.text)
        del recs[-1]
        k=k+2
    records.append(recs)

for i in records:
    for k in i:
        print(k),
    print ("\n")
ch='//*[@id="DgRegist_ctl03_imgDelete"]'

choice=input("Which link do you wish to open?")

if choice==1:
    ch='//*[@id="DgRegist_ctl03_imgDelete"]'
elif(choice==2):
    ch = '//*[@id="DgRegist_ctl04_imgDelete"]'
elif(choice==3):
    ch = '//*[@id="DgRegist_ctl05_imgDelete"]'
elif(choice==4):
    ch = '//*[@id="DgRegist_ctl06_imgDelete"]'
else:
    ch = '//*[@id="DgRegist_ctl07_imgDelete"]'

link=driver.find_element_by_xpath(ch)
link.click()
sleep(2)

html_page=driver.page_source
soup1=BeautifulSoup(html_page,"html.parser")
letters2=soup1.find_all("body")
for i in letters2:
    print i.text
