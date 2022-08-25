from bs4 import BeautifulSoup
import requests
import os
url = "https://urdu.geo.tv/latest-news"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
news_list = soup.find_all('div', class_='entry-title')
headlines = []
for news in news_list:
    if news.find('h2'):
        headlines.append(news.find('h2').text)

imgs = soup.find_all('div', class_='pic')
images = []
for img in imgs:
    if img.find('img'):
        images.append(img.find('img')['src'])

# print(headlines)
print(images)
