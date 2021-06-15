from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen("http://www.yourwebsite.com")
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))