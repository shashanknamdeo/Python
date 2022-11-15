from selenium import webdriver
driver = webdriver.PhantomJS()

import urllib

url = 'https://economictimes.indiatimes.com/archive/year-2002,month-11.cms'

url_content = urllib.parse.urlparse(url)
print(url_content)
# ParseResult(scheme='https', netloc='economictimes.indiatimes.com', path='/archive/year-2002,month-11.cms', params='', query='', fragment='')

host_name = url_content.scheme + '://'+url_content.netloc


Docyear = url_content.path.split('/')[2].split(',')[0].split('-')[1]
DocMonth= url_content.path.split('/')[2].split(',')[1].split('.')[0].split('-')[1]
storeFileName =Docyear+'_'+DocMonth 


driver.get(url)

innerHTML = driver.execute_script("return document.body.innerHTML")

print(type(innerHTML))
from bs4 import BeautifulSoup

content_soup = BeautifulSoup(innerHTML, 'html.parser')

# print(content_soup.prettify())


file = open('../Data/phantomJsData', 'w+', encoding='utf-8')
file.write(str(content_soup.prettify()))
file.close()


# archive_month_link_list = content_soup.find_all('td a')
# Not selecting as I wished 

# This is the css selector method
archive_month_link_list = content_soup.select('td a')


MonthlyLinksFile = open('../Data/MonthlyLinksFile_'+storeFileName, 'w+')

for archive_link in archive_month_link_list:

	if(archive_link.get_text()):   #this check is in place because we get duplicate rows(for the ones which has no date in the cell)
	# print(archive_link)
		# print(archive_link['href'])

		# DocDate = archive_link.get_text()

		MonthlyLinksFile.write(str(host_name+archive_link['href']+'\n'))


MonthlyLinksFile.close()
