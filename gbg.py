import requests
from lxml import etree
import json
from io import StringIO
import re
import ftfy
re.compile('<title>(.*)</title>')

def cgatneworders(casetype, caseno, caseyear):
    if casetype == "Cr.CP":
        number="7"
    elif casetype == "C.P.":
        number="4"
    elif casetype == "M.A.":
        number="3"
    elif casetype == "O.A.":
        number="1"
    elif casetype == "P.T.":
        number="5"
    elif casetype == "R.A.":
        number="6"
    else: number="2"
    url = "http://cgatnew.gov.in/catweb/Delhi/services/upload_order_detail.php"
    params = [
        ("search_type", "1"),
        ("judge_detail", "0"),
        ("from_date", ""),
        ("to_date", ""),
        ("from_date1", ""),
        ("to_date1", ""),
        ("case_type", number),
        ("case_no", caseno),
        ("case_year", caseyear),
        ("txtState", ""),
        ("filing_no", ""),
    ]
    r = requests.post(url=url, params=params)
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(r.text), parser)

    ###########################################Party Detail#############################################
    #ApplicantVSRespondent
    applicantvsrespondent=[]
    try:
        applicantvsrespondent1 = tree.xpath('//table[6]/tr[2]/td/font/text()')
        applicantvsrespondent.append(applicantvsrespondent1[0].strip())
    except:
        pass

    #SerialNumber
    srno=[]
    srno1=tree.xpath('//*[@class="hoverTable"]/tr/td/text()')
    for i in range(0, len(srno1)):
        if srno1[i].strip().isdigit() == True:
            srno.append(srno1[i].strip())

    #CaseNumber
    caseno=[]
    for i in range(4, len(srno)+4):
        caseno1=tree.xpath("//table[6]/tr[{}]/td[2]/text()".format(i))
        caseno.append(caseno1[0].strip())

    #Part Detail
    partydetail=[]
    join=[]
    for i in range(4, len(srno) + 4):
        partydetail1= tree.xpath("//table[6]/tr[{}]/td[3]/text()".format(i))
        join.append(''.join(partydetail1))
        partydetail.append(join[0].strip())
        join=[]

    #Member Name
    membername=[]
    join1=[]
    for i in range(4, len(srno) + 4):
        membername1= tree.xpath("//table[6]/tr[{}]/td[4]/text()".format(i))
        join1.append(''.join(membername1))
        membername.append(join1[0].strip())
        join1=[]


    #Date Of Order
    dateoforder=[]
    join2=[]
    for i in range(4, len(srno) + 4):
        dateoforder1= tree.xpath("//table[6]/tr[{}]/td[5]/text()".format(i))
        join2.append(''.join(dateoforder1))
        dateoforder.append(join2[0].strip())
        join2=[]

    #Remarks
    remarks=[]
    join3=[]
    for i in range(4, len(srno) + 4):
        remarks1 = tree.xpath("//table[6]/tr[{}]/td[6]/text()".format(i))
        join3.append(''.join(remarks1))
        remarks.append(join3[0].strip())
        join3 = []

    #Orders
    join4=[]
    orders_link=[]
    for i in range(4, len(srno) + 4):
        orders1 = tree.xpath("//table[6]/tr[{}]/td[7]/a/@href".format(i))
        print(orders1)
        join4.append(''.join(orders1))
        orders_link.append("http://cgatnew.gov.in/catweb/Delhi/services/" + join4[0])
        join4=[]
    ret_this = {}
    try:
        ret_this['ApplicantVSRespondent'] = applicantvsrespondent
        ret_this['Sr No'] = srno
        ret_this['PARTY DETAIL'] = partydetail
        ret_this[' Member Name'] = membername
        ret_this['Date of Order'] = dateoforder
        ret_this['Remarks'] = remarks
        ret_this['Orders File'] = orders_link
    except:
        pass

    result = json.dumps({"Orders": ret_this})
    print(ftfy.fix_text_encoding(result))

if __name__ == "__main__":
    casetype = input("enter casetype")
    caseno = input("enter caseno")
    caseyear = input("enter year")
    send = cgatneworders(casetype, caseno, caseyear)

