import requests
from bs4 import BeautifulSoup

dayLink = 'https://economictimes.indiatimes.com/archivelist/year-2002,month-11,starttime-37561.cms'
# dayLink = 'https://economictimes.indiatimes.com/archive.cms'



content = requests.get(dayLink).content
soup_content = BeautifulSoup(content, 'html.parser')
soup_prettify = soup_content.prettify()

file = open('../Data/DayLinks', 'w+', encoding='utf-8')
file.write(str(soup_prettify))
file.close()




FilePerDayLink = open('../Data/FilePerDayLink', 'w+')


article_links = soup_content.find_all('ul', class_='content')

# print(len(article_links))
# print(article_links[0])
# article_links has sections in itself


for article_link in article_links:
	for al in article_link.select('li a'):
		# print(al)
		# print(al['href'])
		# print(al.get_text())
		FilePerDayLink.write('https://economictimes.indiatimes.com'+str(al['href'])+'\n')


FilePerDayLink.close()


# al = article_links[1].select('li a')
# for a in al:
# 	print(a.get_text())
# 	print(a['href'])

# article_links = soup_content.select('ul li a')


# for article_link in article_links:
# 	print(article_link)


