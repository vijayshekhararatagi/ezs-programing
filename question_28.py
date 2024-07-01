'''You are given a string containing words separated by spaces. Your task is to write a
function or program that reverses the order of words in the string.
Sample Input:
Hello World
Sample Output:
World Hello'''

inp1=input()
print(*inp1.split()[::-1])