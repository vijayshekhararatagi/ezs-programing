p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
p_w={}
for i in range(len(p)):
    p_w[i]=p[i]/w[i]
print(p_w)
l=list(p_w.items())
sl=sorted(l,reverse=True)
print(sl)