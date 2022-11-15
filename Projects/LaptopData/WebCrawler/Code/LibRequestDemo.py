import requests


DATA_DIR = "../Data/"

# page = requests.get("https://economictimes.indiatimes.com/archive.cms")
page = requests.get('https://docs.python.org/3/')


print(page)
print(page.status_code)
# <Response [200]>
# 200


#page.text and page.content both can be used to access the text of the page, but page.content is used to access the data in bytes.


text = page.text
content = page.content
# print(text)

# print(text.encode('utf-8'))  #converting to encoding('utf-8') results in the content same as in byte formet.[ same as page.content]
# print(content)

# issue with the content, as it is appended by a character 'b'. Why is it so?



# fileText = open(DATA_DIR+'requestDemoText.html', 'w+')

# As the ecomomiesTimes html page contains some unicode character(other than ASCII), thus the encoding needs to be explcitely specified
# while opening the file content for .text, .content was not an isses(as it is just an byte content).
fileText = open(DATA_DIR+'requestDemoText.html', 'w+', encoding='utf-8')
fileContent = open(DATA_DIR+'requestDemoContent.html', 'w+')

fileText.write(str(text))
fileContent.write(str(content))

fileText.close()
fileContent.close()
# data from .content is of the form - b'...data..'. That is it is encoded into quotes and prepended with a b character to signinfies
# that the conent is in bytes format.


# The difference between the .text and .content library is that the in .content data is the content of the response in bytes.
# while .text is Content of the response, in unicode.
# If Response.encoding is None, encoding will be guessed using chardet.

# The encoding of the response content is determined based solely on HTTP headers, following RFC 2616 to the letter. If you can take 
# advantage of non-HTTP knowledge to make a better guess at the encoding, you should set r.encoding appropriately before accessing 
# this property.


# There is some error with the conversion of .text character to string or writing it to file as some unicode characters are not 
# able to be mapped.
#Solved: The error was in writing the .text to the file as some confersion of unicode encoding to the file string was not successfull.
# This is resolved by opening/writing the file with utf-8 encoding.
