from selenium import webdriver
#import time
#from selenium.webdriver.common.keys import Keys
import urllib.request as urllib2
import pandas as pd 

from bs4 import BeautifulSoup
searchquery = input("Enter the search query")
search_query = searchquery.replace(' ', '+') #structuring our search query for search url.


response1 = urllib2.urlopen("https://www.1mg.com/search/all?name=" + search_query + "&start=" + str(0))
html_doc1 = response1.read()
response2 = urllib2.urlopen("https://www.medsindia.in/products/search?like=" + search_query )
html_doc2	 = response2.read()

soup1=BeautifulSoup(html_doc1,'lxml')
soup2=BeautifulSoup(html_doc2,'lxml')

names2 = []
names1 = []
prices1 = []
prices2 = []
img1 = []
img2 = []
y=[]

all_medicines=soup1.find('div',class_="row style__grid-container___3OfcL")
all_medicines=all_medicines.div.find_all('div',{'class' : lambda x : x and x.startswith('col')})

for medicine in all_medicines:
	p=medicine.div.a.find_all('div',{'class' : lambda x : x and x.startswith('style__product')})
	prices1.append((p[2].find('div', {'class' : lambda x : x and x.startswith('style__price-tag')})).text)
	names1.append(p[1].text)
	#img1.append((p[0].div.find('img',class_="style__image___Ny-Sa style__loaded___22epL")).attrs['src'])


all_medicines=soup2.find_all('div',class_="product-wrap")
#print(all_medicines)
for medicine in (all_medicines):
	p=medicine.find_all('div',{'class' : lambda x : x and x.startswith('product-row')})
	for i in range(len(p)):
		names2.append((p[i].div.h4.text))
		prices2.append((p[i].div.find('span',class_="mainPrice")).text)
		img2.append(p[i].div.a.img.attrs['src'])
    #x=x.find('div',class_="style__product-pricing___1OxnE")
    #y=x.find('h4',class_="card z-depth-1").text
#    description.append(y)
#    z=x.find('span',class_="product-sale-price").div.text
#    prices2.append(y)
chart1 = pd.DataFrame({'Name': names1,'Price by 1MG': prices1})
chart2 = pd.DataFrame({'Name': names2,'Price by Medsindia': prices2,'Image links': img2})
#print(img2)
#print(description)
print(chart1)
print(chart2)

