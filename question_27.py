'''Pangram is a sentence containing every letter in the English alphabet. Given a string, 
find all characters that are missing from the string, Le., the characters that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz'''

import string
sen=input().lower()
a=list(string.ascii_lowercase)
for i in sen:
    if i in a:
        a.remove(i)
str1=""
print(str1.join(a))