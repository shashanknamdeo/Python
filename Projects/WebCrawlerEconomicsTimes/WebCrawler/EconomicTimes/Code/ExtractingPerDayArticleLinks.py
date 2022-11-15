import requests
from bs4 import BeautifulSoup



ARCHIVAL_DATA_DIR = '../Data/ArchivalData/'
HOST_NAME = ''

PerDayNewsLinks = 'https://economictimes.indiatimes.com/archivelist/year-2001,month-1,starttime-36892.cms'

Year_Month = '2001_1'
Date_Folder =  '1'

content = requests.get(PerDayNewsLinks).content
soup_content = BeautifulSoup(content, 'html.parser')


PerDayArticleLinks = ARCHIVAL_DATA_DIR+Year_Month+'/'+Date_Folder+'/'+'PerDayArticleLinks'
PerDayArticleLinks = open(PerDayArticleLinks, 'w+')


article_links = soup_content.find_all('ul', class_='content')


for article_link in article_links:
	for al in article_link.select('li a'):
		PerDayArticleLinks.write('https://economictimes.indiatimes.com'+str(al['href'])+'\n')


PerDayArticleLinks.close()

