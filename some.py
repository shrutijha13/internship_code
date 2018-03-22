from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from bs4 import BeautifulSoup
import pytesseract
import string

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/Users/shrutijha/Downloads/pyChrome/bin/chromedriver")  # Optional argument, if not specified will search path.
driver.get('http://www.greentribunal.gov.in/search_case_judgement.aspx')
image = driver.find_element_by_id('content2_im')

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