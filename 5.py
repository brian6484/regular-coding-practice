n , m = map(int,input().split())
data = list(map(int,input().split()))
array = [0]*11

for x in data:
    #number of balls for each weight
    array[x] += 1

result = 0
for i in range(1,m+1):
    n -= array[i] #n becomes 4, 2, 0 from initial 5
    result += array[i] *n

print(result)
