# Referenchttps://www.dataquest.io/blog/web-scraping-tutorial-python/e
# https://www.dataquest.io/blog/web-scraping-tutorial-python/

from bs4 import BeautifulSoup
# Beautiful Soup (BS4) is a parsing library that can use different parsers. A parser is simply a program that can 
# extract data from HTML and XML documents.

import requests
import urllib.parse

DATA_DIR = "../Data/"


url = 'https://economictimes.indiatimes.com/archive.cms'
# url = 'https://docs.python.org/3/'

url_content = urllib.parse.urlparse(url)
# print(url_content)
# ParseResult(scheme='https', netloc='economictimes.indiatimes.com', path='/archive.cms', params='', query='', fragment='')

host_name = url_content.scheme + '://'+url_content.netloc
# print(host_name)
# https://economictimes.indiatimes.com/


page = requests.get(url)


text = page.text
content = page.content


# text_soup = BeautifulSoup(text)
# If there is no parser specified, then python will give a warning and use the default parser('html.parser')-this default parser can be
# different for different OS/Environments.



text_soup = BeautifulSoup(text, 'html.parser')
content_soup = BeautifulSoup(content, 'html.parser')
#though the text and content is different(content is in byte form and text is in text form), their BeautifulSoup object are same.


prettify_soup = text_soup.prettify()
#prettify is method to format the file nicely.



# Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about 
# encodings, unless the document doesn't specify an encoding and Beautiful Soup can't autodetect one. 




# print(text_soup)
# print(content_soup)
# print(text_soup.prettify())


fileText = open(DATA_DIR+'soupDemoText.html', 'w+', encoding='utf-8')
fileContent = open(DATA_DIR+'soupDemoContent.html', 'w+', encoding='utf-8')
filePrettify = open(DATA_DIR+'soupPrettify.html', 'w+', encoding='utf-8')



fileText.write(str(text_soup))
fileContent.write(str(content_soup))
filePrettify.write(str(prettify_soup))


fileText.close()
fileContent.close()
filePrettify.close()




# As all the tags are nested, we can move through the structure one level at a time. We can first select all the elements at the top 
# level of the page using the children property of soup. Note that children returns a list generator, so we need to call the list 
# function on it:
# print(list(content_soup.children))



# [type(item) for item in list(soup.children)] 
# [bs4.element.Doctype, bs4.element.NavigableString, bs4.element.Tag]

# As you can see, all of the items are BeautifulSoup objects. The first is a Doctype object, which contains information about the type 
# of the document. The second is a NavigableString, which represents text found in the HTML document. The final item is a Tag object,
#  which contains other nested tags. The most important object type, and the one we’ll deal with most often, is the Tag object.




fileYearMonthLinks = open(DATA_DIR+'fileYearMonthLinks', 'w+')
# This file stores the links correspondinf to the months of each year.


# Searching for tags by Class name

# Economisc archive webpage contains links to all the monthly calender under class 'nortxt'. So the below code extracted that
# links from the page in a list 
archive_month_link_list = content_soup.find_all('a', class_='normtxt')

# print(archive_month_link_list)
# this is a list

for archive_link in archive_month_link_list:
	
	# print(archive_link)
	#  <a class="normtxt" href="/archive/year-2017,month-11.cms">November</a>


	# print(type(archive_link))
	# Each of this link element is of type : <class 'bs4.element.Tag'>

	# print(archive_link.get_text())
	# get_text will extract the text of the link

	# print(archive_link['href'])
	# /archive/year-2017,month-11.cms
	# return href attribute from the archive_link.

	fileYearMonthLinks.write(host_name+str(archive_link['href']+'\n'))


fileYearMonthLinks.close()