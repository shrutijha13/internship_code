import requests
from bs4 import BeautifulSoup

main_url = "http://bombayhighcourt.nic.in/libweb/commission/Law_Commission_Of_India_Reports.html"
response=requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

names_fc=[]
links_fc=[]
names_sc=[]
links_sc=[]
names_tc=[]
links_tc=[]
names_foc=[]
links_foc=[]
names_fifc=[]
links_fifc=[]
names_sixc=[]
links_sixc=[]
names_sevc=[]
links_sevc=[]
names_eigc=[]
links_eigc=[]
names_ninc=[]
links_ninc=[]
names_tenc=[]
links_tenc=[]
names_elec=[]
links_elec=[]
names_twc=[]
links_twc=[]
names_thc=[]
links_thc=[]
names_fourc=[]
links_fourc=[]
names_fiftc=[]
links_fiftc=[]
names_sixtc=[]
links_sixtc=[]
names_sevtc=[]
links_sevtc=[]
names_eigtc=[]
links_eigtc=[]
names_nintc=[]
links_nintc=[]
names_twenc=[]
links_twenc=[]

letters=soup.find_all("a")

#First Commission
i=21
while (i < 34):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_fc.append(s.strip())
names_fc.insert(13,"Reform of Judicial Administration Vol.1")
names_fc.insert(14,"Reform of Judicial Administration Vol.2")

i=21

while(i<36):
    st=letters[i]['href']
    links_fc.append(st)
    i=i+1

#Second commission
i=36
while (i < 45):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_sc.append(s.strip())

i=37

while(i<45):
    st=letters[i]['href']
    links_sc.append(st)
    i=i+1

#Third
i=45
while (i < 52):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_tc.append(s.strip())

i=46

while(i<52):
    st=letters[i]['href']
    links_tc.append(st)
    i=i+1

#Fourth
i=52
while (i < 64):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_foc.append(s.strip())
del names_foc[7]
names_foc.insert(7,"Capital Punishment. Vol.2")

i=53
while(i<64):
    st=letters[i]['href']
    links_foc.append(st)
    i=i+1

#Fifth
i=64
while (i < 71):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_fifc.append(s.strip())

i=65
while(i<71):
    st=letters[i]['href']
    links_fifc.append(st)
    i=i+1

#Sixth
i=71
while (i < 89):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_sixc.append(s.strip())


i=72
while(i<89):
    st=letters[i]['href']
    links_sixc.append(st)
    i=i+1

#Seventh
i=89
while (i < 99):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_sevc.append(s.strip())


i=90
while(i<99):
    st=letters[i]['href']
    links_sevc.append(st)
    i=i+1

#Eigth
i=99
while (i < 110):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_eigc.append(s.strip())


i=100
while(i<110):
    st=letters[i]['href']
    links_eigc.append(st)
    i=i+1

#Ninth
i=110
while (i < 118):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_ninc.append(s.strip())


i=111
while(i<118):
    st=letters[i]['href']
    links_ninc.append(st)
    i=i+1

#Tenth
i=118
while (i < 145):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_tenc.append(s.strip())


i=119
while(i<145):
    st=letters[i]['href']
    links_tenc.append(st)
    i=i+1

#Eleventh
i=145
while (i < 164):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_elec.append(s.strip())


i=146
while(i<164):
    st=letters[i]['href']
    links_elec.append(st)
    i=i+1

#Twelfth
i=164
while (i < 177):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_twc.append(s.strip())


i=165
while(i<177):
    st=letters[i]['href']
    links_twc.append(st)
    i=i+1

#Thirteenth
i=177
while (i < 188):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_thc.append(s.strip())


i=178
while(i<188):
    st=letters[i]['href']
    links_thc.append(st)
    i=i+1

#Fourteenth
names_fourc.append("The Code of Criminal Procedure, 1973 ( Act No. 2 of 1974 ) - Vol. 1")
names_fourc.append("The Code of Criminal Procedure, 1973 ( Act No. 2 of 1974 ) - Vol. 2")
names_fourc.append("The Narcotics Drugs and Psychotropic Substances Act, 1985 ( Act No. 61 of 1985).")
names_fourc.append("The Indian Penal Code - Vol. 1")
names_fourc.append("The Indian Penal Code - Vol. 2")

i=189
while(i<194):
    st=letters[i]['href']
    links_fourc.append(st)
    i=i+1

#Fifteenth
i=194
while (i < 213):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_fiftc.append(s.strip())


i=195
while(i<213):
    st=letters[i]['href']
    links_fiftc.append(st)
    i=i+1

#Sixteenth
names_sixtc.append("The Foreigners (Amendment) Bill, 2000.")
names_sixtc.append("The Arbitration and Conciliation (Amendment) Bill, 2002.")
names_sixtc.append("Law Relating to Arrest.  Part I.")
names_sixtc.append("Law Relating to Arrest.  Part II.")
names_sixtc.append("Recommendations for amending various enactments, both civil and criminal.  Part I.")
names_sixtc.append("Recommendations for amending various enactments, both civil and criminal.  Part II.")
names_sixtc.append("Public Interest Disclosure and Protection of Informers.  Part I.")
names_sixtc.append("Public Interest Disclosure and Protection of Informers.  Part II.")
names_sixtc.append("Article 20(3) of the Constitution of India and Right to Silence.")
names_sixtc.append("Amendment to Section 106 of the Transfer of Property Act, 1882.")
names_sixtc.append("Amendment of Section 6 of the Land Acquisition Act, 1894.")
names_sixtc.append("A Continuum on the General Clauses Act, 1897 with special reference to the admissibility and codification of external aids to interpretation of statutes.")
names_sixtc.append("Legal Education & Professional Training and Proposals for amendments to the Advocates Act, 1961 and the University Grants Commission Act, 1956. Part - I.")
names_sixtc.append("Legal Education & Professional Training and Proposals for amendments to the Advocates Act, 1961 and the University Grants Commission Act, 1956. Part - II.")
names_sixtc.append("Review of the Indian Evidence Act, 1872. Part -I.")
names_sixtc.append("Review of the Indian Evidence Act, 1872. Part -II.")
names_sixtc.append("Review of the Indian Evidence Act, 1872. Part -IIIA.")
names_sixtc.append("Review of the Indian Evidence Act, 1872. Part -IIIB.")
names_sixtc.append("Review of the Indian Evidence Act, 1872. Part -IV.")
names_sixtc.append("Review of the Indian Evidence Act, 1872. Part -V.")

i=214
while(i<234):
    st=letters[i]['href']
    links_sixtc.append(st)
    i=i+1

#Seventeenth
i=234
while (i < 251):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_sevtc.append(s.strip())

i=235
while(i<251):
    st=letters[i]['href']
    links_sevtc.append(st)
    i=i+1

#Eighteenth
i=251
while (i < 287):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_eigtc.append(s.strip())

i=252
while(i<287):
    st=letters[i]['href']
    links_eigtc.append(st)
    i=i+1
del links_eigtc[19]
del links_eigtc[19]
k=202


#Ninteenth
i=287
while (i < 297):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_nintc.append(s.strip())

names_nintc.append("Section 498A IPC")
i=288
while(i<298):
    st=letters[i]['href']
    links_nintc.append(st)
    i=i+1

del links_nintc[4]

#Twentieth
i=298
while (i < 331):
    k = i + 1
    s=""
    letters_new=letters[i].get_text()
    for l in letters_new:
        if(l=="\n"):
            continue
        elif(l=="\r"):
            s=s+" "
        else:
            s=s+l
    i=i+1
    if(s.strip()==""):
        continue
    else:
        names_twenc.append(s.strip())


del names_twenc[1]
names_twenc.insert(1,"Arrears and Backlog : Creating Additional Judicial (wo)manpower")
del names_twenc[2]

i=299
while(i<331):
    st=letters[i]['href']
    links_twenc.append(st)
    i=i+1

del links_twenc[17]
del links_twenc[2]
