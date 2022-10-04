import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
#import sys

punctuation={'.',',',':','"',';','!'}

s="shubham shubham shubham"
s=s.lower()
print(s)
s=word_tokenize(s)
print(s)


for word in s:
    #print(word in punctuation)   
   
    try:
        i=int(word)
        s.remove(word)
    except ValueError:
        if word in punctuation:
            s.remove(word)
        else:
            flag=False
            for char in word:
                if ord('a')<=ord(char)<=ord('z'):
                    flag=True
            if flag==False:
                s.remove(word)

print(s)
"""
for word in s:
    if ord('A')<=ord(word[0])<=ord('Z'):
        word[0]=chr(ord(word[0])+ord('a')-ord('A'))

s='152india'
try:
    i=int(s)
except:
    print('yes')"""
    