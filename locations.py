import urllib.request as urllib2
from bs4 import BeautifulSoup
r=urllib2.urlopen('https://www.1mg.com/cart')
d=r.read()
soup1=BeautifulSoup(d,'lxml')

l={}
#a=soup1.find('div',class_="main-content").div.find_all('div')
a=soup1.find('div',attrs={'class':	'style__city-label___3vex6'})
print(a)