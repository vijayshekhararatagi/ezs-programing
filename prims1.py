graph = [[0, 2, -1, 6, -1],
         [2, 0, 3, 8, 5],
         [-1, 3, 0, -1, 7],
         [6, 8, -1, 0, 9],
         [-1, 5, 7, 9, 0]]

vi=[False]*len(graph)
min_val=float('inf')
x=-1
y=-1
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]==0 or graph[i][j]==-1:
            continue
        elif min_val>graph[i][j]:
            min_val=graph[i][j]
            x=i
            y=j

print(x+1,y+1,min_val)
vi[x]=True
vi[y]=True
mst=[]
mst.append((x+1,y+1,min_val))
print(mst)

while False in vi:
    min_val = float('inf')
    for i in range(len(graph)):
        if vi[i]==True:
            for j in range(len(graph[i])):
                if graph[i][j]==0 or graph[i][j]==-1 or vi[j]==True:
                    continue
                elif min_val>graph[i][j]:
                    min_val=graph[i][j]
                    x=i
                    y=j
    if min_val<float('inf'):
        vi[y]=True
        mst.append((x+1, y+1, min_val))

print(mst)