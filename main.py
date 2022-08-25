from bs4 import BeautifulSoup
import requests,os
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
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

    return jsonify({'headlines': headlines, 'images': images})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)