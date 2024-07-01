'''You work in the message encoding department of a national security agency. Every message
that is sent from or received in your office is encoded. you have a string containing , alpha numeric characters.
of N is squared and the squares are concatenated together to encode the original number.
Your task is to find and return an integer value representing the encoded value of the
number.
input1: An a string  representing the number and chracters 
Output :
Return an integer value representing the encoded value of the number
input format:
"hello 123 good morning"
output:
149'''

def encodeString(s):
    num = ''
    for i in s:
        if i.isnumeric():
            num += str(int(i)**2)
    return num
s = "hello 123 good morning"
print(encodeString(s))