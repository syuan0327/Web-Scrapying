# 爬蟲練習
## 工具
1.  python3.8
2.  [requests]() ==> 負責抓取檔案
3.  [beautifulsoup](https://web.archive.org/web/20170127002045/https://www.crummy.com/software/BeautifulSoup/bs4/doc/) ==> 負責分析requests抓下來的檔案
## 安裝
```
pip install beautifulsoup
```

```
pip install requests
```
## 實作
#### 抓取網站內容
以gooele為例

request.get() ==> download the web's html

BeautifulSoup(news.text,'html.parser') ==> analysis the html code,and build the object

```
from bs4 import BeautifulSoup
import requests
news=requests.get('https://www.google.com/')
soup=BeautifulSoup(news.text,'html.parser')
print(soup.prettify())
```
#### 抓取網站內容結果(省略版)
```
<!DOCTYPE html>
<html itemscope="" itemtype="http://schema.org/WebPage" lang="zh-TW">
 <head>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"/>
  <title>
   Google
  </title>
  </script>
  <div id="mngb">
   <div id="gbar">
    <nobr>
     <b class="gb1">
      搜尋
     </b>
     <a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">
      圖片
     </a>
     <a class="gb1" href="https://maps.google.com.tw/maps?hl=zh-TW&amp;tab=wl">
      地圖
     </a>
     <a class="gb1" href="https://play.google.com/?hl=zh-TW&amp;tab=w8">
      Play
     </a>
     <a class="gb1" href="https://www.youtube.com/?gl=TW&amp;tab=w1">
      YouTube
     </a>
     <a class="gb1" href="https://news.google.com/?tab=wn">
      新聞
     </a>
     <a class="gb1" href="https://mail.google.com/mail/?tab=wm">
      Gmail
     </a>
     <a class="gb1" href="https://drive.google.com/?tab=wo">
      雲端硬碟
     </a>
     <a class="gb1" href="https://www.google.com.tw/intl/zh-TW/about/products?tab=wh" style="text-decoration:none">
      <u>
       更多
      </u>
      »
     </a>

```
