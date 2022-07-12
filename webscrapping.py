import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

datalist = [] 

##function to scrape the website
def scrape_site(URL):

    ##drivers for Firefox browser
    options = webdriver.FirefoxOptions()
    ##not showing the browser on
    options.headless = True
    ##setting the options
    driver = webdriver.Firefox(options=options)

    driver.get(URL)

    ##waiting time for loading the page
    time.sleep(1)

    ##loop for going through all the pages (50 pages)
    for page in range(0,50):

        #get the tag elements <ol> with class equals 'row'
        element = driver.find_element(By.XPATH, "//ol[@class='row']")
        html = element.get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        #looking for all <article> tags with class equals 'product_pod'
        datas = soup.find_all('article', {'class': 'product_pod'})
        
        #going through 'datas' and appending in the data list as dictionary 
        for item in datas:
            
            data = {
                    'title': item.find('h3').text,
                    'price': item.find('p', {'class': 'price_color'}).text,
                    ##getting the class name, not the content
                    'stars': item.find('p', {'class': 'star-rating'})['class'][1],
                    'available': item.find('p', {'class': 'instock'}).text
                }
            datalist.append(data)
        
        #stop at page 50 'cause there is no next page
        if page == 49: break
        #click in the next page
        driver.find_element(By.XPATH,"//ul[@class='pager']/li[@class='next']/a").click()

    ##close the Firefox
    driver.close()

scrape_site('https://books.toscrape.com/catalogue/page-1.html')

#making a data frame with json 
df = pd.DataFrame(datalist)
##saving as CSV file
df.to_csv('data_book.csv', index = False, sep=';')