from collections import Counter
hola = list(map(int, input().split()))
Counter(hola)
acount = hola.count(0)
bcount = hola.count(1)
result = 0

print(acount,bcount,result)