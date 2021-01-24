import requests
import urllib
from urllib import request
import bs4
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
url = 'https://www.chiphell.com/thread-2292308-1-1.html'
x = 1
xxx = requests.get(url=url,headers=headers)
print(xxx)
soup = bs4.BeautifulSoup(xxx.text,"html.parser")
yyy = soup.find_all('img')
for zzz in yyy:
    link = zzz.get('zoomfile')
    #print(link)
    if link != None:
       links =link
       urllib.request.urlretrieve(links,'H:\桌面\折腾\pic\%s.jpg'%x)
       x+=1
       print("下载中")
    
        

    
