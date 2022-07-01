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
    return jsonify({'data':headlines})

app.run(debug=True)