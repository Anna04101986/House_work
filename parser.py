import requests
from bs4 import BeautifulSoup as bs
import random

class Parser:
    @staticmethod
    def parser(url: str):
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        congratulations = soup.find_all('p', class_="sfst")
        congratulations = [c.text for c in congratulations]
        random.shuffle(congratulations)
        return congratulations


if __name__ == '__main__':
    print(Parser.parser('https://pozdravok.com/pozdravleniya/den-rozhdeniya/'))
