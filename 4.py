t = int(input())
data = list(map(int,input().split()))
data.sort()
target = 1

for i in data:
    if i>target:
        break
    else:
        target += i

print(target)

