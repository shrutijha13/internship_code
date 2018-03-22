from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from bs4 import BeautifulSoup
import pytesseract
import string
from selenium.webdriver.common.by import By
import json

def captcha_to_text():
    image = driver.find_element_by_id('captcha')

    driver.save_screenshot("ss.png")
    location = image.location
    size = image.size

    element = Image.open("ss.png")

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = element.crop((left, top, right, bottom))
    image.save("captcha.png")

    pytesseract.pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/3.05.01/bin/tesseract"
    a = Image.open("/Users/shrutijha/Documents/sel/captcha.png")
    s = str(pytesseract.image_to_string(a))

    str1 = ''
    l = list(string.ascii_lowercase)
    l1 = list(string.ascii_uppercase)
    for i in s:
        if (i in l1):
            str1 = str1 + i.lower()
        elif (i in l):
            str1 = str1 + i
        else:
            continue

    captcha_text = driver.find_element_by_id("userEnteredCaptcha")
    captcha_text.send_keys(str1)
    driver.find_element_by_id("companyLLPMasterData_0").click()

def is_element_present(how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException: return False
    return True

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/Users/shrutijha/Downloads/pyChrome/bin/chromedriver")  # Optional argument, if not specified will search path.
driver.get('http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do')

sleep(2)
driver.find_element_by_id("imgSearchIcon").click()
company_name=driver.find_element_by_id("searchcompanyname")
sleep(2)
company=raw_input("Enter company name you want to search :")
company_name.send_keys(company)

driver.find_element_by_id("findcindata").click()
sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")
letters=soup.find_all("table",attrs={'class': 'result-forms'})
#print(letters)
link_texts=[]

for i in letters:
    p=i.find_all("a")
    for k in p:
        link_texts.append(k.text)
k=1
for i in link_texts:
    print k,i
    k=k+1

choice=input("Which link do you want to see :")

driver.find_element_by_link_text(link_texts[choice-1]).click()
sleep(2)

captcha_to_text()
a=is_element_present(By.ID, "msgboxclose")

while(a==True):
    sleep(1)
    driver.find_element_by_id("msgboxclose").click()
    captcha_to_text()
    a = is_element_present(By.ID, "msgboxclose")

sleep(2)
html_page=driver.page_source
soup=BeautifulSoup(html_page,"html.parser")
letters1=soup.find_all("table",attrs={'class': 'result-forms'})

s=''
for i in letters1:
    s=s+i.text

dict={}
dict[company]=s
results=json.dumps(dict)
print results