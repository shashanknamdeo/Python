from selenium import webdriver
# from urllib2 import urlopen
from urllib.request import urlopen


# url = 'http://www.google.com'
url = 'https://economictimes.indiatimes.com/archive.cms'
file_name = '../Data/test.txt'

conn = urlopen(url)
content = conn.read()
conn.close()


# print(data)
print(type(content))

from bs4 import BeautifulSoup
content_soup = BeautifulSoup(content, 'html.parser')

print(content_soup.prettify())


# file = open(file_name,'w+')
# file.write(str(data))
# file.close()

# browser = webdriver.Firefox()
# browser = webdriver.Firefox()
# browser.get('file:///'+file_name)
# html = browser.page_source
# browser.quit()