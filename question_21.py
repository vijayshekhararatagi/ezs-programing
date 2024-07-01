def encodeString(s):
    l=[]
    num = ''
    for i in s:
        if i.isnumeric():
            l.append(str(int(i)**2))
    return (num.join(l))
s = "hello 129 good morning"
print(encodeString(s))