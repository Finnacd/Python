import requests
from bs4 import BeautifulSoup
res = requests.get('https://wenku.baidu.com/list/175?l=4.3.6')
res.encoding = 'gb2312'
soup = BeautifulSoup(res.text,'html.parser')
for con in soup.select('.hasb'):
    a = con.select("a")[0]['href']
    title = con.select("a")[0].text
    print(" "+title+"链接：https://www.baidu.com"+a)