from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.etsy.com/search?q=crochet%20pillow")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"currency-value"})
for name in nameList:
    print(name.get_text())
