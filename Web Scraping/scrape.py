import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories(hn):
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


def custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[i].select('.score')
        if len(votes):
            point = int(votes[0].getText().replace(' points', ''))
            if point > 99:
                hn.append({'title': title, 'href': href, 'votes': point})
    return hn


def main():
    i = 1
    news_list = []
    while i < 3:
        res = requests.get(f'https://news.ycombinator.com/news?p={i}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titlelink')
        subtext = soup.select('.subtext')
        news_list.extend(custom_hn(links, subtext))
        i += 1
    news = sort_stories(news_list)
    pprint.pprint(news)

if __name__ == '__main__':
    main()
