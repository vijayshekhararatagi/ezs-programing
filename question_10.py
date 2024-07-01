def OperationsBinaryString(str):
    a=int(str[0])
    i=1
    while(i<len(str)):
        if(str[i]=="A"):
            a=a&int(str[i+1])
        elif(str[i]=="B"):
            a=a|int(str[i+1])
        else:
            a=a^int(str([i+1]))
        i=i+2
    return a
    r=input()
print(OperationsBinaryString(str))