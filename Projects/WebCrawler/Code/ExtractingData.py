import requests
from bs4 import BeautifulSoup
import urllib


# url = 'https://economictimes.indiatimes.com/articleshow/26901551.cms'
# url = 'https://economictimes.indiatimes.com/articleshow/26902578.cms'

url = 'https://economictimes.indiatimes.com/news/economy/policy/kelkar-panel-may-retain-i-t-rates-but-raise-limit/articleshow/26877563.cms'

content = requests.get(url).content

content_soup = BeautifulSoup(content, 'html.parser')
prettify_soup = content_soup.prettify()
# print(prettify_soup)



DataFile = open('../Data/DataFile', 'w+', encoding='utf-8')
DataFile.write(str(prettify_soup))
DataFile.close()



# print(content_soup.select('.Normal'))
# returns a list

# print(len(content_soup.select('.Normal')))
# 1

print(content_soup.select('.Normal')[0].text)