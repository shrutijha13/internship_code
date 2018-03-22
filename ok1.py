import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PIL import Image
#import org.openqa.selenium.WebElement;

driver = webdriver.Chrome("/Users/shrutijha/Downloads/pyChrome/bin/chromedriver")  # Optional argument, if not specified will search path.
driver.get('http://services.ecourts.gov.in/ecourtindia/cases/case_no.php?state=D&state_cd=26&dist_cd=3')
'''
a=raw_input("Enter court complex:")
b=raw_input("Enter case type:")
c=raw_input("Enter case number:")
d=raw_input("Enter case year:")
'''
court_complex=Select(driver.find_element_by_id("court_complex_code"))
court_complex.select_by_visible_text("Karkardooma Court Complex")
case_ty=Select(driver.find_element_by_id("case_type"))
case_ty.select_by_visible_text("ARBTN CASES")

search_box1 = driver.find_element_by_id("search_case_no")
search_box1.send_keys("6")
search_box2 = driver.find_element_by_id("rgyear")
search_box2.send_keys("2016")

image= driver.find_element_by_tag_name('img')
#img1=image.get_attribute('src')
#print(img1)
driver.save_screenshot("ss.png")
location=image.location
size=image.size

element=Image.open("ss.png")

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

image = element.crop((left, top, right, bottom))
image.show()
image.save("captcha.png")

e=raw_input("Enter the captcha text you see:")
captcha_text=driver.find_element_by_id("captcha")
captcha_text.send_keys(e)

driver.find_element_by_name("submit1").click()

#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()