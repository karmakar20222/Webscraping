from urllib import response
from bs4 import BeautifulSoup 
import pandas as pd
import requests
import csv

url ='https://www.flipkart.com/search?q=oneplus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=oneplus+mobile%7CMobiles&requestId=3621f978-11b7-40c0-8142-6a4c1867eeb0&as-searchtext=oneplus'

response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")
# print(soup.prettify)

names =[]
prices = [] 
datas = []
product = soup.find('div',attrs={'class':'_4rR01T'})
# print(product.text)

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    
    # name = a.find('div',attrs={'class':'_4rR01T'})
    name = a.find('div',attrs={'class':'_4rR01T'})
    price = a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})

    datas.append({'Name':name.text,'Price':price.text})


df = pd.DataFrame(datas)
df.to_csv('product.csv')