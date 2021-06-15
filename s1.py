from urllib.request import urlopen


myURL=urlopen("http://www.google.com/")
print(myURL.read())