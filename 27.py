n,x=map(int,input().split())
data = list(map(int,input().split()))
count = 0
for i in data:
    if i==x:
        count +=1

if count==0:
    print(-1)
else:
    print(count)
