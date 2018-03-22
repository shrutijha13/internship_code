from requestium import Session,Keys

s = Session(webdriver_path='/Users/shrutijha/Downloads/pyChrome/bin/chromedriver',
            browser='chrome',
            #default_timeout=15,
            #webdriver_options={'arguments': ['headless']}
             )

response=s.get('http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do')