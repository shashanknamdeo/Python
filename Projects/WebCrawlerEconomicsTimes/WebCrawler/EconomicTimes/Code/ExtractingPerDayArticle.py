import requests
from bs4 import BeautifulSoup
import urllib


url = 'https://economictimes.indiatimes.com/news/economy/policy/kelkar-panel-may-retain-i-t-rates-but-raise-limit/articleshow/26877563.cms'

content = requests.get(url).content

content_soup = BeautifulSoup(content, 'html.parser')



DataFile = open('../Data/DataFile', 'w+', encoding='utf-8')
DataFile.write(str(prettify_soup))
DataFile.close()

print(content_soup.select('.Normal')[0].text)