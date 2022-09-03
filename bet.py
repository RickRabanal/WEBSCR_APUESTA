from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time

ubicacion= "C:/Users/rraba/Downloads/chromedriver" #Ruta del driver
driver= webdriver.Chrome(ubicacion)

home_link="https://www.ebay.com/"
search_kw="iphone x".replace(" ","+")

driver.get(home_link+"sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw="+search_kw+"&_sacat=0")

page=BeautifulSoup(driver.page_source,'html.parser')

for phone in page.findAll('li', attrs={'class':'s-item','data-view':True}):
    title=phone.find('div',attrs={'class':'s-item__title'}).text
    print(title)
    price=phone.find('span',attrs={'class':'s-item__price'}).text
    print(price)

