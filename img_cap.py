import urllib.request
import os
from bs4 import BeautifulSoup

url = 'http://image.baidu.com/'
res = urllib.request.urlopen(url)
res.encoding = 'utf-8'
html = res.read()
#print(html)
soup = BeautifulSoup(html,'html.parser')
result = soup.find_all('img')
#print(res)
links = []
index = 0
for content in result:
    if index < 100:
        s = content.get('src')
        if s is None:
            ss= s
        else:
            links.append(s.split(' ')[0])

    index += 1
print(len(links))
if not os.path.exists('photo'):
    os.makedirs('photo')
i=0;
for link in  links:
    filename = 'photo\\'+'photo'+str(i)+'.jpg'
    with open(filename,'w'):
        urllib.request.urlretrieve(link,filename)