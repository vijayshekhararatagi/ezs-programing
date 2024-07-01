"happy fathers day"
'''extract the vowel which has max count'''
'''a,e,i,o,u=0'''

from collections import Counter
str = "hello worlde"
str = list(str)
for i in str:
    if i in "aeiou":
        s = i
        break
str.remove(s)
s1 = str.index(s)
print(s1+1)

