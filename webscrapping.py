import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

datalist = [] 

##function to scrape the website
def scrape_site():

    ##drivers for Firefox browser
    options = webdriver.FirefoxOptions()
    ##not showing the browser on
    options.headless = True
    ##setting the options
    driver = webdriver.Firefox(options=options)

    categories = ['travel_2',
    'mystery_3',
    'historical-fiction_4',
    'sequential-art_5',
    'classics_6',
    'philosophy_7',
    'romance_8',
    'womens-fiction_9',
    'fiction_10',
    'childrens_11',
    'religion_12',
    'nonfiction_13',
    'music_14',
    'default_15',
    'science-fiction_16',
    'sports-and-games_17',
    'add-a-comment_18',
    'fantasy_19',
    'new-adult_20',
    'young-adult_21',
    'science_22',
    'poetry_23',
    'paranormal_24',
    'art_25',
    'psychology_26',
    'autobiography_27',
    'parenting_28',
    'adult-fiction_29',
    'humor_30',
    'horror_31',
    'history_32',
    'food-and-drink_33',
    'christian-fiction_34',
    'business_35',
    'biography_36',
    'thriller_37',
    'contemporary_38',
    'spirituality_39',
    'academic_40',
    'self-help_41',
    'historical_42',
    'christian_43',
    'suspense_44',
    'short-stories_45',
    'novels_46',
    'health_47',
    'politics_48',
    'cultural_49',
    'erotica_50',
    'crime_51']

    for category in categories:
        URL = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
        driver.get(URL)

        ##waiting time for loading the page
        time.sleep(1)

        ##loop for going through all the pages
        while True:

            #get the tag elements <ol> with class equals 'row'
            element = driver.find_element(By.XPATH, "//div[@class='col-sm-8 col-md-9']")
            html = element.get_attribute('outerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            #looking for all <article> tags with class equals 'product_pod'
            datas = soup.find_all('article', {'class': 'product_pod'})
            #getting the category (this one is processed)
            categ = soup.find('h1').text
            
            #going through 'datas' and appending in the data list as dictionary 
            for item in datas:
                
                data = {
                        'title': item.find('h3').text,
                        'category': categ,
                        'price': item.find('p', {'class': 'price_color'}).text,
                        ##getting the class name, not the content
                        'stars': item.find('p', {'class': 'star-rating'})['class'][1],
                        'available': item.find('p', {'class': 'instock'}).text
                    }
                datalist.append(data)
            
            #try if there is another page if not it will break
            try:
                #click in the next page
                driver.find_element(By.XPATH,"//ul[@class='pager']/li[@class='next']/a").click()
                continue
            except Exception:
                break

        
    ##close the Firefox   
    driver.close()

scrape_site()

#making a data frame with json 
df = pd.DataFrame(datalist)
##saving as CSV file
df.to_csv('data_book.csv', index = False, sep=';')