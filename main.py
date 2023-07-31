import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find('a'))
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hn(link, votes):
    hn = []
    for idx, item in enumerate(link):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        points = votes[idx].getText
        hn.append({'title': title, 'links':href})
        if len(vote):
            points = int(vote[0].getText().replace())
            if ponts > 100:
                hn.append({'title' : title, 'link': href, 'votes':ponts })
    return sort_by_votes(hn)

print.print(create_custom_hn(links, votes))
