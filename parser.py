import requests
from bs4 import BeautifulSoup
import json

data = {}


def start_pars(url):
    r = requests.get(url=url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        heading = soup.find('div', class_='row header-box').find('div', class_='col-md-8').text
        print(heading)
        quotes = soup.find_all('div', class_='quote')
        for one_quote in quotes:
            quote = one_quote.findNext('span', class_='text').text
            author = one_quote.findNext('small', class_='author').text
            tags = one_quote.findNext('div', class_='tags').find_all('a')
            tags_text = []
            for tag in tags:
                t = tag.text
                tags_text.append(t)
            data[author] = {
                'text_quote': quote,
                'author': author,
                'tags': tags_text
            }
        print(data)
    with open('results.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def main():
    url = 'https://quotes.toscrape.com/'
    start_pars(url)


if __name__=='__main__':
    main()