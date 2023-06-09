# -*- coding: utf-8 -*-
"""suryaprakash_day46_diy_solution_doc

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18HN9EFuiyBTo-ImUTJ5jEXpVK4ZkUsXG

Perform the following tasks to get an understanding of stemming,lemmatization andWord Sense Disambiguation (WSD) using the Natural LanguageTool Kit (NLTK) 1.Declare   a   list   of   words   and   perform   stemming   on   each   word   using PorterStemmer() andLancasterStemmer()2.Declare a sentence and perform lemmatization on each word of the sentence using  WordNetLemmetizer()3.Declare two different sentences with homonyms and perform WSD to fetch the meanings of the homonyms in the context of their respective sentencesNote:Homonyms  are  words  with  the  exact  spelling  and  pronunciation  but different meanings.
"""

wordlist=['friend','friendship','friends','friendships','stabil','destabilize','misunderstanding','railroad','moonlight','football']
print('the original list is:',wordlist)

from nltk.stem.lancaster import LancasterStemmer
import nltk
from nltk.stem import PorterStemmer
pst=PorterStemmer()
lan=LancasterStemmer()
for word in wordlist:
  print(word,pst.stem(word),lan.stem(word))

sent='He was running and eating at the same time. He had a bad habit of swimming after long hours of playing in the sun.'
pun="?':!.,;"
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wl=WordNetLemmatizer()
sw=nltk.word_tokenize(sent)
for word in sw:
  if word in pun:
   sw.remove(word)
for word in sw:
 print(word,wl.lemmatize(word))

import nltk
nltk.download('punkt')
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
sent1='This device is used to jam the signal'
sent2='I am stuck in a traffic jam'
a=(lesk(word_tokenize(sent1),'jam'))
print(a,a.definition())
b=(lesk(word_tokenize(sent2),'jam'))
print(b,b.definition())