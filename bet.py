from tkinter import E
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time

ubicacion= 'xxxxxxxx' #Ruta del driver
driver= webdriver.chorme(ubicacion)
