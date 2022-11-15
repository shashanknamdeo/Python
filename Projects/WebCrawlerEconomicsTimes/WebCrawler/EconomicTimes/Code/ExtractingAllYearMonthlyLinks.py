import requests
from bs4 import BeautifulSoup
import urllib.parse


DATA_DIR = "../Data/"
ARCHIVE_FILE_NAME = 'ArchiveLink'
ALL_YEAR_MONTHLY_LINKS_FILE = 'AllYearMonthlyLinks' 

HOST_NAME = ''

with open(DATA_DIR + ARCHIVE_FILE_NAME, 'r') as ArchiveLinkFile:
	ArchiveLink = ArchiveLinkFile.readline()


url_content = urllib.parse.urlparse(ArchiveLink)
HOST_NAME = url_content.scheme + '://'+url_content.netloc


page_content = requests.get(ArchiveLink).content
soup_content = BeautifulSoup(page_content, 'html.parser')


AllYearMonthlyLinks = open(DATA_DIR+ALL_YEAR_MONTHLY_LINKS_FILE, 'w+')

archive_month_link_list = soup_content.find_all('a', class_='normtxt')

for archive_link in archive_month_link_list:
	AllYearMonthlyLinks.write(HOST_NAME+str(archive_link['href']+'\n'))

AllYearMonthlyLinks.close()
