from urllib.request import urlopen
html = urlopen("https://docs.python.org/3/")

DATA_DIR = '../Data/'

content =html.read()
print(content)


file = open(DATA_DIR+'requestDemo.html', 'w+')
file.write(str(content))
file.close()




import os
import urllib.parse as urlparse
url = "http://photographs.500px.com/kyle/09-09-201315-47-571378756077.jpg"
a = urlparse.urlparse(url)

print(a)
# ParseResult(scheme='http', netloc='photographs.500px.com', path='/kyle/09-09-201315-47-571378756077.jpg', params='', query='', fragment='')

print(a.netloc)
print(a.scheme)
print(a.path)
# photographs.500px.com
# http
# /kyle/09-09-201315-47-571378756077.jpg


