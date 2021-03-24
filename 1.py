n = int(input())
hola = list(map(int, input().split()))
hola.sort()
group = 0 
count = 0

for i in range(n):
    count = 1
    if count >= i:
        group = 1
        count = 0
print(group)



