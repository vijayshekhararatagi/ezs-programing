'''You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0'''

def checkPassword(str,s):
    n = 0
    c = 0
    sp = 0
    if s < 4:
        return False
    if str[0].isnumeric():
        return False
    for i in str:
        if i.isnumeric():
            n = 1
        if i == " " and i == "/":
            sp = 1
        if i.isupper():
            c = 1
    if n == 1 and c == 1 and sp == 0:
        return True
    else:
        return False
str = input()
s = len(str)
print(checkPassword(str,s))
    
