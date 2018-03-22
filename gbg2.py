import requests
from lxml import etree
import json
from io import StringIO
from datetime import datetime
from bs4 import BeautifulSoup
import ftfy
import re
re.compile('<title>(.*)</title>')

#URL:http://cms.nic.in/ncdrcusersWeb/login.do?method=caseStatus
#caseno:CC/123/2017

def ncdrcorder(casetype, caseno, caseyear):
    caseno = str(casetype) + '/' + str(caseno) + '/' + str(caseyear)
    caseidin = "0/0/{}".format(caseno)
    url = "http://cms.nic.in/ncdrcusersWeb/ViewProceedingCS.jsp"
    params = [
     ("method",	"ViewProceedingCS"),
     ("fano",	caseno),
     ("case_id_in", ""),
     ("dtOfHearing", ""),
     ("courtId",	""),
     ("cid",	caseidin),
     ("stateCode",	"0"),
     ("distCode",	"0"),
    ]
    r = requests.post(url=url, params = params)
    parser = etree.HTMLParser()
    tree   = etree.parse(StringIO(r.text), parser)

    #Date Of hearing
    dateOfHearing = []
    try:
        hearing2 = tree.xpath('//*[@class="rptnumhval"]/text()')
        for i in range(0, len(hearing2), 2):
            if hearing2[i] != " ":
                date1 = tree.xpath('//*[@class="rptnumhval"]/text()')[i]
                ofhearing = date1.strip()
                if ofhearing != "":
                    dateOfHearing.append(ofhearing)
    except:
        pass

    #datereverse
    datereversed1 = []
    try:
        for i in range(0, len(dateOfHearing)):
            datereversed = datetime.strptime(dateOfHearing[i], '%d/%m/%Y').strftime('%Y-%m-%d')
            datereversed1.append(datereversed)

    except: pass

    #orders
    orders = []
    try:
        for i in range(0, len(datereversed1)):
            url3 = "http://cms.nic.in/ncdrcusersWeb/servlet/confonet.courtroom.GetDailyOrder"
            payload1 = {'case_id_in': caseidin, 'dtofhearing': datereversed1[i], 'method': 'GetProceedings', 'orderflag':	'D'}
            r3 = requests.post(url=url3, params=payload1)
            a1 = BeautifulSoup(r3.text, "lxml").text
            print(a1)
            orders.append(re.sub(r'[^\x00-\x7F]+', ' ',a1.replace('\n', '').replace('\r', '').replace('&nbsp', '').replace('Daily Order', '')))


    except: pass


    ret_this = {}
    try:
        ret_this['Orders'] = orders
    except: pass


    result = json.dumps({"Orders" : ret_this})
    print (ftfy.fix_text_encoding(result))

b=ncdrcorder("CC", "297", "2017")