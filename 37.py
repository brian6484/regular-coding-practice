INF = int(1e9)
n= int(input())
m= int(input())
graph = [[INF]*(n+1)for _ in range(n+1)]

for a in range (1,n+1):
    for b in range (1,n+1):
        if a ==b:
            graph[a][b] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    #since graph[a][b] is inf, it will satisfy below condition always unless another shouter route(c) appears and updates c
    if c <graph[a][b]:
        graph[a][b] = c #update value in 2d list
    # floyd
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] ==INF:
            print(0)
        else:
            print(graph[a][b])
    print()