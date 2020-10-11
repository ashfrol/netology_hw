import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['дизайн', 'mkdir', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
bs = BeautifulSoup(response.text, 'html.parser')

keywords = set(KEYWORDS)

articles = bs.find_all('article', class_='post post_preview')


for article in articles:
    article_id_href = article.find('a', class_='btn btn_x-large btn_outline_blue post__habracut-btn').attrs.get(
        'href')
    response_article_text = requests.get(article_id_href)
    bs_text = BeautifulSoup(response_article_text.text, 'html.parser')
    article_text = bs_text.find('div', id='post-content-body').text
    result_preview = re.split('\.*\,*\:*\s+', article.text)
    result_preview = list(result_preview)
    result_text = re.split('\.*\,*\:*\s+', article_text)
    result_text = list(result_text)
    result = set(result_preview + result_text)

    if keywords.intersection(result):
        time = article.find('span', class_='post__time').text
        title = article.find('a', class_='post__title_link').text
        link = article.find('a', class_='post__title_link').attrs.get('href')
        print(f'<{time}> - <{title}> - <{link}>')
