import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

cookies = {'over18': '1'}

res = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())