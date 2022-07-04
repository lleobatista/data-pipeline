import requests
from bs4 import BeautifulSoup

dataslist = []

def get_datas(page):
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    datas = soup.find_all('article', {'class': 'product_pod'})
    
    for item in datas:
        data = {
            'title': item.find('h3').text,
            'price': item.find('p', {'class': 'price_color'}).text,
            'stars': item.find('p', {'class': 'star-rating'})['class'][1],
            'available': item.find('p', {'class': 'instock'}).text
        }
        dataslist.append(data)
    return

for i in range(1,51):
    get_datas(i)

print(dataslist)