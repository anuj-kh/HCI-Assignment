import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver.chrome.options import Options

table = pd.DataFrame([], columns=['Website', 'Link', 'Network operator', 'Link Load time', 'Link dead or not'])
table2 = pd.DataFrame([], columns=['Website', 'Network operator', 'Average Link Load time', 
                                    'Number of dead links', 'Number of working links', 'Website score'])

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'performance':'ALL' }
chrome_options = Options()
chrome_options.add_experimental_option('w3c', False)

driver = webdriver.Chrome(desired_capabilities=d, options=chrome_options)

websites = ['https://nrega.nic.in/netnrega/home.aspx', 'https://www.usa.gov/', 'https://www.bits-pilani.ac.in/', 'https://www.isro.gov.in/', 'https://medium.com/' ]

for website in websites:
    j=0
    driver.get(website)

    links=driver.find_elements_by_xpath('.//a')

    for i in range(len(links)):
        links[i] = links[i].get_attribute('href')

    for a in links:
        Link_Load_Time = 0
        for k in range(5):
            if(a!="javascript:void(0);" and a!="javascript:void(0)"):
                try:
                    driver.get(a)
                    performance_log = driver.get_log('performance')
                    for i in performance_log:
                        y = json.loads(i['message'])
                        if y['message']['method']=="Network.responseReceived":
                            status=y['message']['params']['response']['status']
                            status=(int)(status/100)
                except:
                    status=4
                if status<4:
                    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
                    domComplete = driver.execute_script("return window.performance.timing.domComplete")
                    Link_Load_Time += domComplete - navigationStart
        
        Link_Load_Time = Link_Load_Time/5
        if status<4:        
            if j == 0:
                table.loc[len(table.index)] = [website, a, 'Airtel', Link_Load_Time, 'N']
            else:
                table.loc[len(table.index)] = ['', a, 'Airtel', Link_Load_Time, 'N']
        else:
            if j == 0:
                table.loc[len(table.index)] = [website, a, 'Airtel', '0', 'Y']
            else:
                table.loc[len(table.index)] = ['', a, 'Airtel', '0', 'Y']

        j += 1

    table.loc[len(table.index)] = ['', '', '', '', '']

table.to_csv('table1.csv',index=False)        

driver.close()