from selenium import webdriver
browser = webdriver.Chrome()

from selenium.webdriver.chrome.options import Options


url = 'https://economictimes.indiatimes.com/archive/year-2002,month-11.cms'
browser.get(url)

innerHTML = browser.execute_script("return document.body.innerHTML")
# print(innerHTML)

print(type(innerHTML))
from bs4 import BeautifulSoup

content_soup = BeautifulSoup(innerHTML, 'html.parser')

print(content_soup.prettify())


file = open('../Data/seleniumData', 'w+', encoding='utf-8')
file.write(str(content_soup.prettify()))
file.close()


# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(chrome_options=chrome_options)
# print(driver.get(url))