import sys
def cost(curr,visited,G,Dp):
    n=len(G)
    if len(visited)==n:
        return G[curr][0]
    visit=tuple(visited)
    if (curr,visit) in Dp:
        return Dp[(curr,visit)]
    min_cost=sys.maxsize
    for i in range(n):
        if i not in visited:
            new_visit=visited+[i]
            new_cost=G[curr][i]+cost(i,new_visit,G,Dp)
            min_cost=min(min_cost,new_cost)
    Dp[(curr,visit)]=min_cost
    return min_cost

G=[
    [0,4,7,5,5],
    [4,0,2,3,8],
    [7,2,0,3,4],
    [5,3,3,0,6],
    [5,8,5,6,0]
]
n=len(G)
Dp={}
print("Minimum Cost",cost(0,[0],G,Dp))