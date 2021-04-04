t = int(input())
data = list(map(int,input().split()))
data.sort()
target = 1

for i in data:
    if i>target: #if 357, i = 3 > 1(target) so break and ans is 1
        break
    else:
        target += i

print(target)

