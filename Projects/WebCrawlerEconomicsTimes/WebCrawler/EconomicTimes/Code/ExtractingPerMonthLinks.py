from selenium import webdriver
driver = webdriver.PhantomJS()

import urllib
import os
from bs4 import BeautifulSoup




ARCHIVAL_DATA_DIR = '../Data/ArchivalData/'
HOST_NAME = ''

MonthlyLinkURL = 'https://economictimes.indiatimes.com/archive/year-2001,month-1.cms'

url_content = urllib.parse.urlparse(MonthlyLinkURL)
HOST_NAME = url_content.scheme + '://'+url_content.netloc


Docyear = url_content.path.split('/')[2].split(',')[0].split('-')[1]
DocMonth= url_content.path.split('/')[2].split(',')[1].split('.')[0].split('-')[1]
Year_Month =Docyear+'_'+DocMonth 


Monthly_Archive_Dir = ARCHIVAL_DATA_DIR + Year_Month
if not os.path.exists(Monthly_Archive_Dir):
    os.makedirs(Monthly_Archive_Dir)




driver.get(MonthlyLinkURL)
innerHTML = driver.execute_script("return document.body.innerHTML")

soup_content = BeautifulSoup(innerHTML, 'html.parser')
archive_month_link_list = soup_content.select('td a')

PerDayNewsLinks = open(ARCHIVAL_DATA_DIR+Year_Month+'/' + 'PerDayNewsLinks', 'w+')

for archive_link in archive_month_link_list:
	if(archive_link.get_text()):
		PerDayNewsLinks.write(str(HOST_NAME+archive_link['href']+','+archive_link.get_text()+'\n'))


PerDayNewsLinks.close()
