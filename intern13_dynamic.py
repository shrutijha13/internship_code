import requests
import time

ds=input("Enter district:")
ps=input("Enter police station:")
y=input("Enter year:")
f_no=input("Enter FIR no.:")

def calc(ds,ps):
    if(ds=="CENTRAL"):
        sdis_no = 8162
        if(ps=="ANAND PARBAT"):
            sps_no=8162001
        elif(ps=="CHANDNI MAHAL"):
            sps_no=8162008
        elif(ps=="D.B.G. ROAD"):
            sps_no=8162038
        elif (ps == "DARYA GANJ"):
            sps_no = 8162010
        elif (ps == "HAUZ QAZI"):
            sps_no = 8162015
        elif (ps == "I.P.ESTATE"):
            sps_no = 8162016
        elif (ps == "JAMA MASJID"):
            sps_no = 8162019
        elif (ps == "KAMLA MARKET"):
            sps_no = 8162023
        elif (ps == "KAROL BAGH"):
            sps_no = 8162026
        elif (ps == "NABI KARIM"):
            sps_no = 8162016
        elif (ps == "PAHAR GANJ"):
            sps_no = 8162041
        elif (ps == "PATEL NAGAR"):
            sps_no = 8162042
        elif (ps == "PRASAD NAGAR"):
            sps_no = 8162040
        elif (ps == "RAJINDER NAGAR"):
            sps_no = 8162045
        else:
            sps_no = 8162056
    elif(ds=="CRIME BRANCH"):
        sdis_no=8175
        sps_no=8175001
    elif(ds=="DWARKA"):
        sdis_no=8176
        if(ps=="BABA HARIDAS NAGAR"):
            sps_no=8176009
        elif(ps=="BINDA PUR"):
            sps_no=8176001
        elif (ps == "CHHAWALA"):
            sps_no = 8176007
        elif (ps == "DWARKA SOUTH"):
            sps_no = 8176003
        elif (ps == "DABRI"):
            sps_no = 8176002
        elif (ps == "DWARKA NORTH"):
            sps_no = 8176004
        elif (ps == "JAFFARPUR KALAN"):
            sps_no = 8176006
        elif (ps == "NAJAF GARH"):
            sps_no = 8176010
        elif (ps == "SECTOR 23 DWARKA"):
            sps_no = 8176005
        else:
            sps_no = 8176008
    elif(ds=="EAST"):
        sdis_no = 8168
        if(ps == "GHAZIPUR"):
            sps_no = 8168010
        elif (ps == "JAGAT PURI"):
            sps_no = 8168014
        elif (ps == "KALYANPURI"):
            sps_no = 8168013
        elif (ps == "MADHU VIHAR"):
            sps_no = 8168023
        elif (ps == "MANDAWLI FAZAL PUR"):
            sps_no = 8168024
        elif (ps == "MAYUR VIHAR PH-1"):
            sps_no = 8168026
        elif (ps == "NEW ASHOK NAGAR"):
            sps_no = 8168028
        elif (ps == "PANDAV NAGAR"):
            sps_no = 8168050
        elif (ps == "PREET VIHAR"):
            sps_no = 8168030
        else:
            sps_no = 8168041
    elif(ds=="EOW"):
        sdis_no = 8956
        sps_no = 8956001
    elif(ds=="METRO"):
        sdis_no = 8160
        if(ps=="IGI AIRPORT METRO"):
            sps_no= 8160004
        elif(ps=="JANAK PURI METRO"):
            sps_no = 8160010
        elif(ps=="KASHMIRI GATE METRO"):
            sps_no = 8160007
        elif(ps=="Metro Police Station Azadpur"):
            sps_no = 8160015
        elif(ps=="Metro Police Station Ghitorni"):
            sps_no = 8160003
        elif(ps=="Metro Police Station Nangloi"):
            sps_no = 8160009
        elif (ps == "Metro Police Station Netaji Subash Place"):
            sps_no = 8160016
        elif(ps=="Metro Police Station OKhla Vihar"):
            sps_no = 8160002
        elif(ps=="Metro Police Station Pragati Maidan"):
            sps_no = 8160014
        elif (ps == "Metro Police Station Rajiv Chowk"):
            sps_no = 8160012
        elif (ps == "Nehru Place Metro"):
            sps_no = 8160013
        elif (ps == "RAJA GARDEN METRO"):
            sps_no = 8160008
        elif (ps == "RITHALA METRO"):
            sps_no = 8160005
        elif (ps == "SHASHTRI PARK METRO"):
            sps_no = 8160006
        else:
            sps_no = 8160001
    elif(ds=="NEW DELHI"):
        sdis_no = 8165
        if (ps == "BARAKHAMBA ROAD"):
            sps_no = 8165002
        elif (ps == "CHANKYA PURI"):
            sps_no = 8165007
        elif (ps == "CONNAUGHT PLACE"):
            sps_no = 8165011
        elif (ps == "IITF,Pragati Maidan"):
            sps_no = 8165012
        elif (ps == "MANDIR MARG"):
            sps_no = 8165015
        elif (ps == "NORTH AVENUE"):
            sps_no = 8165038
        elif (ps == "PARLIAMENT STREET"):
            sps_no = 8165022
        elif (ps == "SOUTH AVENUE"):
            sps_no = 8165037
        elif (ps == "TILAK MARG"):
            sps_no = 8165035
        else:
            sps_no = 8165036
    elif (ds == "NORTH"):
        sdis_no = 8166
        if (ps == "BARA HINDU RAO"):
            sps_no = 8166004
        elif (ps == "BURARI"):
            sps_no = 8166052
        elif (ps == "CIVIL LINES"):
            sps_no = 8166007
        elif (ps == "GULABI BAGH"):
            sps_no = 8166024
        elif (ps == "KASHMERI GATE"):
            sps_no = 8166016
        elif (ps == "KOTWALI"):
            sps_no = 8166018
        elif (ps == "LAHORI GATE"):
            sps_no = 8166023
        elif (ps == "MAURICE NAGAR"):
            sps_no = 8166010
        elif (ps == "ROOP NAGAR"):
            sps_no = 8166031
        elif (ps == "SADAR BAZAR"):
            sps_no = 8166038
        elif (ps == "SARAI ROHILLA"):
            sps_no = 8166039
        elif (ps == "SUBZI MANDI"):
            sps_no = 8166041
        else:
            sps_no = 8166051
    elif (ds == "NORTH EAST"):
        sdis_no = 8173
        if (ps == "BHAJAN PURA"):
            sps_no = 8173005
        elif (ps == "GOKUL PURI"):
            sps_no = 8173054
        elif (ps == "HARSH VIHAR"):
            sps_no = 8173055
        elif (ps == "JAFRABAD"):
            sps_no = 8173058
        elif (ps == "JYOTI NAGAR"):
            sps_no = 8173056
        elif (ps == "KARAWAL NAGAR"):
            sps_no = 8173016
        elif (ps == "KHAJURI KHAS"):
            sps_no = 8173015
        elif (ps == "NAND NAGRI"):
            sps_no = 8173025
        elif (ps == "NEW USMANPUR"):
            sps_no = 8173030
        elif (ps == "SEELAMPUR"):
            sps_no = 8173042
        elif (ps == "SONIA VIHAR"):
            sps_no = 8173057
        else:
            sps_no = 8173045
    elif (ds == "NORTH WEST"):
        sdis_no = 8172
        if (ps == "ADARSH NAGAR"):
            sps_no = 8172003
        elif (ps == "ASHOK VIHAR"):
            sps_no = 8172006
        elif (ps == "BHARAT NAGAR"):
            sps_no = 8172007
        elif (ps == "BHALSWA DAIRY"):
            sps_no = 8172008
        elif (ps == "JAHANGIR PURI"):
            sps_no = 8172014
        elif (ps == "KESHAV PURAM"):
            sps_no = 8172025
        elif (ps == "MAHENDRA PARK"):
            sps_no = 8172051
        elif (ps == "MAURYA ENCLAVE"):
            sps_no = 8172049
        elif (ps == "MODEL TOWN"):
            sps_no = 8172017
        elif (ps == "MUKHERJEE NAGAR"):
            sps_no = 8172030
        elif (ps == "RANI BAGH"):
            sps_no = 8172050
        elif (ps == "SHALIMAR BAGH"):
            sps_no = 8172035
        elif (ps == "SUBHASH PLACE"):
            sps_no = 8172047
        else:
            sps_no = 8172036
    elif(ds=="OUTER DISTRICT"):
        sdis_no = 8174
        if (ps == "AMAN VIHAR"):
            sps_no = 8174008
        elif (ps == "BABA HARIDAS NAGAR(OLD)"):
            sps_no = 8174018
        elif (ps == "KANJHAWALA"):
            sps_no = 8174010
        elif (ps == "MANGOL PURI"):
            sps_no = 8174005
        elif (ps == "MIANWALI NAGAR"):
            sps_no = 8174023
        elif (ps == "MUNDKA"):
            sps_no = 8174025
        elif (ps == "NAJAF GARH(OLD)"):
            sps_no = 8174019
        elif (ps == "NANGLOI"):
            sps_no = 8174021
        elif (ps == "NIHAL VIHAR"):
            sps_no = 8174022
        elif (ps == "PASCHIM VIHAR"):
            sps_no = 8174024
        elif (ps == "RANHOLA"):
            sps_no = 8174020
        else:
            sps_no = 8174011
    elif (ds == "PALAM AIRPORT"):
        sdis_no= 8169
        if(ps=="DOMESTIC AIRPORT"):
             sps_no = 8169001
        else:
             sps_no = 8169002
    elif (ds == "RAILWAYS"):
        sdis_no = 8164
        if (ps == "ANAND VIHAR RLY STN"):
            sps_no = 8164004
        elif (ps == "DELHI CANTT. RAILWAY STATION"):
            sps_no = 8164041
        elif (ps == "HAZRAT NIZAMUDDIN RLY STN"):
            sps_no = 8164032
        elif (ps == "NEW DELHI RLY. STN."):
            sps_no = 8164026
        elif (ps == "OLD DELHI (DELHI MAIN) RLY. STN."):
            sps_no = 8164025
        elif (ps == "SARAI ROHILLA STATION"):
            sps_no= 8164034
        else:
            sps_no= 8164042
    elif (ds == "ROHINI"):
        sdis_no = 8959
        if (ps == "ALIPUR"):
            sps_no = 8959004
        elif (ps == "BAWANA"):
            sps_no = 8959001
        elif (ps == "BEGUM PUR"):
            sps_no = 8959003
        elif (ps == "K.N. KATJU MARG"):
            sps_no = 8959007
        elif (ps == "NARELA"):
            sps_no = 8959005
        elif (ps == "NORTH ROHINI"):
            sps_no = 8959011
        elif (ps == "PRASHANT VIHAR"):
            sps_no = 8959008
        elif (ps == "SAMAIPUR BADLI"):
            sps_no = 8959006
        elif (ps == "SHAHBAD DAIRY"):
            sps_no = 8959002
        elif (ps == "SOUTH ROHINI"):
            sps_no = 8959010
        else:
            sps_no = 8959009
    elif (ds == "SHAHDARA"):
        sdis_no = 8957
        if (ps == "ANAND VIHAR"):
            sps_no = 8957002
        elif (ps == "FARSH BAZAR"):
            sps_no = 8957006
        elif (ps == "G.T.B. ENCLAVE"):
            sps_no = 8957009
        elif (ps == "GANDHI NAGAR"):
            sps_no = 8957004
        elif (ps == "GEETA COLONY"):
            sps_no = 8957005
        elif (ps == "KRISHNA NAGAR"):
            sps_no = 8957003
        elif (ps == "MANSAROVAR PARK"):
            sps_no = 8957008
        elif (ps == "SEEMAPURI"):
            sps_no = 8957010
        elif (ps == "SHAHDARA"):
            sps_no = 8957007
        else:
            sps_no = 8957001
    elif(ds=="SOUTH"):
        sdis_no = 8167
        if(ps=="AMBEDKAR NAGAR"):
            sps_no= 8167064
        elif(ps=="CHITRANJAN PARK"):
            sps_no = 8167062
        elif(ps=="DEFENCE COLONY"):
            sps_no = 8167010
        elif(ps=="FATEHPUR BERI"):
            sps_no = 8167012
        elif(ps=="GREATER KAILASH"):
            sps_no = 8167061
        elif(ps=="HAUZ KHAS"):
            sps_no = 8167017
        elif (ps == "K.M. PUR"):
            sps_no = 8167023
        elif(ps=="LODI COLONY"):
            sps_no = 8167028
        elif(ps=="MALVIYA NAGAR"):
            sps_no = 8167033
        elif (ps == "MEHRAULI"):
            sps_no = 8167032
        elif (ps == "NEB SARAI"):
            sps_no = 8167057
        elif (ps == "R.K. PURAM(OLD)"):
            sps_no = 8167041
        elif (ps == "SAFDARJUNG ENCLAVE"):
            sps_no = 8167047
        elif (ps == "SAKET"):
            sps_no = 8167056
        elif(ps=="SANGAM VIHAR"):
            sps_no = 8167063
        elif(ps=="SAROJINI NAGAR"):
            sps_no = 8167046
        elif (ps == "SOUTH CAMPUR(OLD)"):
            sps_no = 8167011
        elif (ps == "VASANT KUNJ NORTH(OLD)"):
            sps_no = 8167058
        elif (ps == "VASANT KUNJ SOUTH(OLD)"):
            sps_no = 8167060

        else:
            sps_no = 8167059
    elif (ds == "SOUTH WEST"):
        sdis_no = 8171
        if (ps == "BINDA PUR(OLD)"):
            sps_no = 8171004
        elif (ps == "DABRI(OLD)"):
            sps_no = 8171010
        elif (ps == "DELHI CANTT"):
            sps_no = 8171011
        elif (ps == "CHHAWALA(OLD)"):
            sps_no = 8171058
        elif (ps == "DWARKA NORTH(OLD)"):
            sps_no = 8171015
        elif (ps == "DWARKA SOUTH(OLD)"):
            sps_no = 8171014
        elif (ps == "JAFFARPUR KALAN(OLD)"):
            sps_no = 8171020
        elif (ps == "KAPASHERA"):
            sps_no = 8171030
        elif (ps == "PALAM VILLAGE"):
            sps_no = 8171057
        elif (ps == "R.K. PURAM"):
            sps_no = 8171060
        elif (ps == "SAGAR PUR"):
            sps_no = 8171054
        elif (ps == "SECTOR 23 DWARKA(OLD)"):
            sps_no = 8171016
        elif (ps == "SOUTH CAMPUS"):
            sps_no = 8171061
        elif (ps == "UTTAM NAGAR(OLD)"):
            sps_no = 8171059
        elif (ps == "VASANT KUNJ NORTH"):
            sps_no = 8171062
        elif (ps == "VASANT KUNJ SOUTH"):
            sps_no = 8171063

        else:
            sps_no = 8171064
    elif (ds == "SOUTH-EAST"):
        sdis_no = 8955
        if (ps == "AMAR COLONY"):
            sps_no = 8955007
        elif (ps == "AMBEDKAR NAGAR(OLD)"):
            sps_no = 8955015
        elif (ps == "BADARPUR"):
            sps_no = 8955012
        elif (ps == "CHITRANJAN PARK(OLD)"):
            sps_no = 8955010
        elif (ps == "GOVIND PURI"):
            sps_no = 8955002
        elif (ps == "GREATER KAILASH(OLD)"):
            sps_no = 8955008
        elif (ps == "HAZARAT NIZAMUDDIN"):
            sps_no = 8955005
        elif (ps == "JAIT PUR"):
            sps_no = 8955001
        elif (ps == "JAMIA NAGAR"):
            sps_no = 8955004
        elif (ps == "KALKAJI"):
            sps_no = 8955009
        elif (ps == "LAJPAT NAGAR"):
            sps_no = 8955006
        elif (ps == "NEW FRIENDS COLONY"):
            sps_no = 8955003
        elif (ps == "OKHLA INDUSTRIAL AREA"):
            sps_no = 8955013
        elif (ps == "PUL PRAHLAD PUR"):
            sps_no = 8955017
        elif (ps == "SANGAM VIHAR(OLD)"):
            sps_no = 8955014
        elif (ps == "SARITA VIHAR"):
            sps_no = 8955011

        else:
            sps_no = 8955016
    elif(ds=="SPECIAL CELL(SB)"):
        sdis_no=8954
        sps_no=8954001
    elif(ds=="SPECIAL POLICE UNIT"):
        sdis_no=8953
        sps_no=8953001
    elif(ds=="VIGILANCE"):
        sdis_no=8161
        sps_no=8161001
    else:
        sdis_no = 8170
        if (ps == "HARI NAGAR"):
            sps_no = 8170015
        elif (ps == "INDER PURI"):
            sps_no = 8170064
        elif (ps == "JANAK PURI"):
            sps_no = 8170021
        elif (ps == "KHYALA"):
            sps_no = 8170062
        elif (ps == "KIRTI NAGAR"):
            sps_no = 8170025
        elif (ps == "MAYAPURI"):
            sps_no = 8170028
        elif (ps == "MOTI NAGAR"):
            sps_no = 8170029
        elif (ps == "NARAINA"):
            sps_no = 8170063
        elif (ps == "PUNJABI BAGH"):
            sps_no = 8170043
        elif (ps == "RAJOURI GARDEN"):
            sps_no = 8170037
        elif (ps == "TILAK NAGAR"):
            sps_no = 8170051
        else:
            sps_no= 8170060

    return sdis_no,sps_no

sdis_no,sps_no=calc(ds,ps)

headers={'Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Host':'59.180.234.21:8080','Content-Length':'125'}
url = "http://59.180.234.21:8080/citizen/regfirsearchpage.htm"
payload='sdistrict='+str(sdis_no)+'&spolicestation='+str(sps_no)+'&firFromDateStr=&firToDateStr=&regFirNo='+f_no+'&radioValue=undefined&searchName=&firYear='+y

i = 0
while(i<100):
    try:
        r = requests.post(url, headers=headers, params=payload)
        break
    except:
        time.sleep(1)
        i+=1


p=r.json()

date=[]
record_created_on=[]
firNumDisp=[]
pdf_link=[]

for i in p['list']:
    date.append(i['firRegDate'])
    record_created_on.append(i["recordCreatedOn"])
    firNumDisp.append(i["firNumDisplay"])
    pdf_link.append("https://docs.google.com/viewer?url=http://59.180.234.21:8080/citizen/gefirprint.htm?firRegNo="+i["firRegNum"])

if(date==[]):
    print("No record exists")
else:
    print("FIR NUMBERS:",firNumDisp)
    print("FIR DATES:",date)
    print("RECORDS CREATED ON:",record_created_on)
    print("FIR LINKS",pdf_link)



