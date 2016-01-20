__author__ = 'Mike'
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

#  acquire keywords list
keywords_o = open('keywords.txt','r')
keywords = keywords_o.read()
keywords_o.close()
words = keywords.split("\n")
t = PrettyTable(['Title', 'Link'])

def start():
    url = 'http://seattle.craigslist.org/search/zip'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.find_all('a', attrs={'class': 'hdrlnk'}):
        try:
            href = "http://seattle.craigslist.org" + link.get('href')
            title = link.string
            for keyword in words:
                if keyword in title:
                    t.add_row([title, href])

        except(UnicodeEncodeError):
            pass
    print(t)



start()
