t = int(input())
array = list(map(int,input().split()))
for i in range(t):
    if array[i] == i:
        print(i)
