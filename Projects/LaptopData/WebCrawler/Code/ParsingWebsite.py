import requests
from bs4 import BeautifulSoup
url='https://www.geeksforgeeks.org'
r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')
#to find all paragraph
soup.find_all('p')
#to find first paragraph
soup.find('p')
#to find all anchors (hyperlinks)
soup.find_all('a')
#to find title
soup.title
#to find all links
list1=soup.find_all('a')
for l in list1:
    l['href']
# to find all the links having text 'Algorithms'
list1=soup.find_all('a')
for l in list:
    if 'Algorithms' in l.text:
    	l
