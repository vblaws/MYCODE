from bs4 import BeautifulSoup
import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

for start_num in range(0, 250, 25):
    respon = requests.get(
        f'https://movie.douban.com/top250?start={start_num}', headers=header)
    if respon.ok:
        html = respon.text
        soup = BeautifulSoup(html, "html.parser")
        all_title = soup.find_all("span", attrs={"class": "title"})
        for title in all_title:
            title_string = title.string
            if "/" not in title_string:
                print(title_string)
    else:
        print("请求失败")
