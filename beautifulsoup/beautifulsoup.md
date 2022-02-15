# 爬蟲練習-BeautifulSoup用法
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
### 抓取網站內容
以gooele為例

request.get() ==> download the web's html

BeautifulSoup(news.text,'html.parser') ==> analysis the html code,and build the object

```python
from bs4 import BeautifulSoup
import requests
news=requests.get('https://www.google.com/')
soup=BeautifulSoup(news.text,'html.parser')
print(soup.prettify())# 輸出排版後的 HTML 程式碼
```
抓取網站內容結果(省略版)：
```html
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
### 抓取標籤內的內容(抓取標籤節點)
#### 一、 可以使用 `soup.標籤名`：

 ##### 1. soup.標籤名
 以title為例，原本該行的html程式碼為：<title>Google</title>
 
 我們可以使用以下的程式碼：
  ```python
  print(soup.title)
  ```
 抓取title標籤的結果：
  ```
  <title>Google</title>
  ```
 ##### 2. soup.標籤名.string
 如果想要只顯示title標籤內(Google)的字可以將程式改成以下(加上.string)：
  ```python
  print(soup.title.string)
  ```
 ##### 3. soup.a 示範
 2.同理，如果是想抓取a標籤當中的內容我們可以打 `soup.a`：
  ```python
  print(soup.a)
  ```
 抓取結果：
  ```
  <a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">圖片</a> 
  ```

#### 二、 除了以上方法，我們也可以使用 `soup.find('標籤名')`：

##### 1.以`<a>`為例：
 ```python
 a=soup.find('a')
 print(a) 
 ```
##### 抓取結果：
 ```
 <a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">圖片</a>
 ```
### 提取節點屬性(get)
把 href裡面的內容印出來
```python
a=soup.find('a')
print(a.get('href'))
``` 
所以這邊會把`href`後面的結果印出來：
```
https://www.google.com.tw/imghp?hl=zh-TW&tab=wi
```
### 搜尋多個節點(find_all)
 
我們可以從抓取結果看到，以上兩中方法 `soup.標籤名`和 `soup.find('標籤名')`都只能抓取該頁面出現的第一筆，那我們該如何抓取很多筆資料呢?
##### 1. 找尋所有符合搜尋節點的資料
可以使`find_all('標籤名')`列出所有該搜尋標籤名的所有資料，在使用迴圈將每筆資料列出：
 ```python
 results=soup.find_all('a')
 for result in results:
    print(result)
    print('\n')
 ```
##### 結果：
```
<a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">圖片</a>
<a class="gb1" href="https://maps.google.com.tw/maps?hl=zh-TW&amp;tab=wl">地圖</a>
<a class="gb1" href="https://play.google.com/?hl=zh-TW&amp;tab=w8">Play</a>
<a class="gb1" href="https://www.youtube.com/?gl=TW&amp;tab=w1">YouTube</a>
<a class="gb1" href="https://news.google.com/?tab=wn">新聞</a>
<a class="gb1" href="https://mail.google.com/mail/?tab=wm">Gmail</a>
<a class="gb1" href="https://drive.google.com/?tab=wo">雲端硬碟</a>
<a class="gb1" href="https://www.google.com.tw/intl/zh-TW/about/products?tab=wh" style="text-decoration:none"><u>更多</u> »</a>
<a class="gb4" href="http://www.google.com.tw/history/optout?hl=zh-TW">網頁記錄</a>
<a class="gb4" href="/preferences?hl=zh-TW">設定</a>
<a class="gb4" href="https://accounts.google.com/ServiceLogin?hl=zh-
...以下省略
```
##### 2. 找尋特定屬性，EX:id,class_
如果是想要搜尋節點中的class屬性，可以使用以下用法，比較需要注意的是 `class`需要打成 `class_`
```python
results=soup.find_all('a',class_='gb1')
for result in results:
    print(result)
```
##### 結果：
會跑出`a`節點標籤當中`class`屬性為`gb1`的所有選項：
```
<a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">圖片</a>
<a class="gb1" href="https://maps.google.com.tw/maps?hl=zh-TW&amp;tab=wl">地圖</a>
<a class="gb1" href="https://play.google.com/?hl=zh-TW&amp;tab=w8">Play</a>
<a class="gb1" href="https://www.youtube.com/?gl=TW&amp;tab=w1">YouTube</a>
<a class="gb1" href="https://news.google.com/?tab=wn">新聞</a>
<a class="gb1" href="https://mail.google.com/mail/?tab=wm">Gmail</a>
<a class="gb1" href="https://drive.google.com/?tab=wo">雲端硬碟</a>
<a class="gb1" href="https://www.google.com.tw/intl/zh-TW/about/products?tab=wh" style="text-decoration:none"><u>更多</u> »</a>
```
##### 3. 限制找尋數量
此外我們可以使用`limit`來限制結果抓取數量，結果因篇幅關係就不貼在這了，有興趣可以試試看。：
```python
results=soup.find_all('a',class_='gb1',limit=3)
for result in results:
    print(result)
```
##### 4. 找尋多個標籤
```python
results=soup.find_all(['a','b'],limit=2)
for result in results:
    print(result)
```
##### 結果：
```
<b class="gb1">搜尋</b>
<a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">圖片</a>
```

