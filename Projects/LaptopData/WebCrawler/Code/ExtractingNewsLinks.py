"""
This script takes a archive url of EconomicTimes, and extracts the news links fro each date.

sample url : https://economictimes.indiatimes.com/archive/year-2002,month-11.cms
each type of the above urls point a webpage containing the calender. THe dates beside the calender stores the link to the news webpage.
That news webpage link is used to extract the news link per date.


"""


from bs4 import BeautifulSoup
import requests

DATA_DIR = "../Data/EconomicTimesData/"
url = 'https://economictimes.indiatimes.com/archive/year-2002,month-11.cms'

content = requests.get(url).content
content_soup = BeautifulSoup(content, 'html.parser')

# archive_month_link_list = content_soup.find_all('a', class_='normtxt')

calendarData = open(DATA_DIR+'calendarData', 'w+', encoding='utf-8')
prettify_soup = content_soup.prettify()
calendarData.write(str(prettify_soup))
calendarData.close()



