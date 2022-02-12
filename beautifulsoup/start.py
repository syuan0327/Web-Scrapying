from calendar import c
from bs4 import BeautifulSoup
import requests
#use request.get() to store web's html
news=requests.get('https://www.google.com/')
#analysis the html code,and build the object
soup=BeautifulSoup(news.text,'html.parser')
#output the html content
print(soup.prettify())
'''
#<title>Google</title>
print(soup.title)
#Google,string只取文字
print(soup.title.string)
#base on the html label to research the content 
#use 'H3' label
print('#################################################################################')
a=soup.find('a')#找一個
print(a)
print('#################################################################################')
#itemprop要查找的類型<h3 itemprop="headline">
#limit要找幾個
results=soup.find_all('a',limit=5)#找全部或限制數量
for result in results:
    print(result.string)
    print('\n')

print('#################################################################################')
results=soup.find_all(['a','b'],limit=2)#找全部或限制數量
for result in results:
    print(result)
    print('\n')
#用tag(input)結合屬性(id)查詢
results = soup.find_all('input', id="gbv")
print(results)
#用屬性查詢
results = soup.find(id="footer")
print(results)

print('#################################################################################')
a=soup.find_all('div')
for i in a:
    if i.find('a')==None:
        continue
    else:
        print(i.select_one('a').get('href'))
        print('\n')
        '''