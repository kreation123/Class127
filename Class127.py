from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv 
startUrl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\basuk\Downloads\chromedriver_win32")
browser.get(startUrl)
time.sleep(10)
def screpe():
    headers = ["Name","Light Years From Earth","Planet Mass","STELLAR MAGNITUDE	",'DISCOVERY DATE']
    planetData = []
    for i in range(0.428):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all("ul",attrs={'class','exoplanet'}):
            li_tags = ul_tag.find_all('li')
            path = "//*[@id="page"]/section[1]/div"

screpe()
