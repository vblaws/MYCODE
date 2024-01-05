from bs4 import BeautifulSoup
import requests

respon = requests.get('https://ssr1.scrape.center/')

if respon.ok:
    html = respon.text
    soup = BeautifulSoup(html, 'html.parser')
    all_title = soup.find_all('h2', attrs={'class': 'm-b-sm'})
    for title in all_title:
        print(title.string)
