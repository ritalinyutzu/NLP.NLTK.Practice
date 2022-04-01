'''兩種不同的詞幹還原法, NLTK v.s. SpaCy'''

#詞形還原是將一個字的各種形式轉換成他的基本單字,或者字典標題字(lemma),類似詞幹提取的定義,但不太相同。一樣都是形容詞 "better"
#NLTK還原的結果與SpaCy還原的結果不同,分別是good和well,兩個都是正確的。
#詞形還原需要對單字及其上下文進行語言分析,執行的時間也比詞幹提取還長。
#NLTK與SpaCy通常只選其一,以便整個pipeline處理都使用同一種框架

#NTLK
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("better",pos='a')) # a是形容詞
'''>>>result: good '''

#SpaCy
import spacy
sp = spacy.load('en_core_web_sm')
token = sp(u'better')
for word in token:
    print(word.text,word.lemma_)
'''>>>result: better well '''

'''辨識名字需要進行POS標注'''

# POS 標注
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Charles Spencer Chaplin was born on 16 April 1889 toHannah Chaplin(born Hannah Harriet Pedlingham Hill) and Charles Chaplin Sr')
for token in doc:
          print(token.text,token.lemma_,token.pos_,
               token.shape_,token.is_alpha,token.is_stop)
'''>>>result:
Charles Charles PROPN Xxxxx True False
Spencer Spencer PROPN Xxxxx True False
Chaplin Chaplin PROPN Xxxxx True False
was be AUX xxx True True
born bear VERB xxxx True False
on on ADP xx True True
16 16 NUM dd False False
April April PROPN Xxxxx True False
1889 1889 NUM dddd False False
toHannah toHannah PROPN xxXxxxx True False
Chaplin(born Chaplin(born PROPN Xxxxx(xxxx False False
Hannah Hannah PROPN Xxxxx True False
Harriet Harriet PROPN Xxxxx True False
Pedlingham Pedlingham PROPN Xxxxx True False
Hill Hill PROPN Xxxx True False
) ) PUNCT ) False False
and and CCONJ xxx True True
Charles Charles PROPN Xxxxx True False
Chaplin Chaplin PROPN Xxxxx True False
Sr Sr PROPN Xx True False
'''
