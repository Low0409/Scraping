
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.at-time.com/index.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")


print(soup.find_all("img"))

# print(text)