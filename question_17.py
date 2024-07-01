'''
Problem Statement:
In a quaint village nestled between rolling hills, there were N different salt containers
and N different pepper containers in two separate groups. Each container had a
specific level of bitterness, represented by arrays A and B respectively. The task at
hand was to form N combinations, each consisting of one salt container and one
pepper container
However, there was a twist to the challenge. The objective was to arrange the
combinations in such a way that the maximum bitterness level, which is the sum of
salt and pepper quantities in each combination, was minimized.
Print the lowest possible maximum bitterness level.
Input Format:
The first line contains a single integer N, the number of salt and pepper containers in
each group.
The second line contains N space-separated integers, denoting the bitterness level of
N salt containers.
The third line contains N space-separated integers, denoting the bitterness level of N 
Sample Innput:
3
1 3 5
2 8 6
Sample Output:
11
'''

N=int(input())
S=list(map(int,input().split()))
P=list(map(int,input().split()))
F=[]
for i in range(0,N-1):
    a = S[i]+P[i]
    F.append(a)
print(max(F))