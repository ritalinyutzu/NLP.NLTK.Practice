#nltk套件要先裝比較久
import nltk
nltk.download()

#內建直接import就好
import urllib.request
response = urllib.request.urlopen('http://www.taipeitimes.com/')
html = response.read()
print(html)

from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://www.taipeitimes.com/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")

#記得安裝html5lib模組
text = soup.get_text(strip=True)
#print(text)
tokens = text.split()
#print(tokens)

import nltk
freq = nltk.FreqDist(tokens)

freq.plot(20, cumulative=False) #畫出了一堆垃圾需要被停用的詞

#開始停用詞彙
from nltk.corpus import stopwords
stopwords.words('english')
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)

#停用完重新繪圖，稍微正常一點，但還是有一些符號需要去掉
freq = nltk.FreqDist(clean_tokens)
freq.plot(20,cumulative=False)
