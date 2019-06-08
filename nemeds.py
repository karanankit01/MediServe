from selenium import webdriver

search_query = input("Enter the search query")
search_query = search_query.replace(' ', '+') #structuring our search query for search url.

executable_path="/path/to/firfox"
from selenium.webdriver.firefox.options import Options
options=Options()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)
from bs4 import BeautifulSoup
med=[]
browser.get("https://www.netmeds.com/catalogsearch/result/?q=" + search_query + "&start=0")
html_doc=browser.page_source

soup=BeautifulSoup(html_doc,'lxml')

all_medicines=soup.find_all('div',class_="ais-infinite-hits--item")


images=[]

names=[]

prices=[]

for medicine in all_medicines:
    medicine=medicine.div.div.div
    image=medicine.div.div.img.attrs['src']
    images.append(str(image)[2:])

    desc=medicine.find('div' , class_="result-sub-content")

    name=desc.a.h3.text
    for i in range (2,500):
       if ord(name[i]) !=32:
            a=i
            break
    for i in range (len(name)-1,2,-1):
        if ord(name[i]) !=32:
            b=i
            break

    name=name[a:b-1]
    names.append(name)

    price=desc.div.div.find('div' , class_="price").div.div.span.text

    for i in range (3,500):
        if ord(price[i]) !=32:
            a=i
            break
    for i in range (len(price)-1,2,-1):
        if ord(price[i]) !=32:
            b=i
            break

    price=price[a:b]
    prices.append(price)



print(images)
print(names)
print(prices)

