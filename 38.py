INF = int(1e9)
n= int(input())
m= int(input())
graph = [[INF]*(n+1)for _ in range(n+1)]

for a in range (1,n+1):
    for b in range (1,n+1):
        if a ==b:
            graph[a][b] = 0
for _ in range(m):
    a,b = map(int,input().split())
    #since graph[a][b] is inf, it will satisfy below condition always unless another shouter route(c) appears and updates c
    graph[a][b] =1

    # george floyd
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
count =0
# i dont get this
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count +=1
        if count == n:
            result +=1
print(result)

