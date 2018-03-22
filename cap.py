from PIL import Image
import pytesseract
import string

pytesseract.pytesseract.tesseract_cmd="/usr/local/Cellar/tesseract/3.05.01/bin/tesseract"
a=Image.open("/Users/shrutijha/Documents/sel/captcha.png")
s=(pytesseract.image_to_string(a))
s=s.encode('utf-8')
print s

'''
print s
str1=''
l=list(string.ascii_lowercase)
l1=list(string.ascii_uppercase)
for i in s:
    if(i in l1):
        str1=str1+i.lower()
    elif(i in l):
        str1=str1+i
    else:
        continue
print str1
'''