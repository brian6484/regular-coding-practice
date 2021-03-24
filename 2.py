hola = list(map(int, input().split()))
result = 1

for i in range(1,len(hola)):
    a = hola[i]+hola[i+1]
    b = hola[i]*hola[i+1]
    if a >= b:
        result += a
    elif a <= b:
        result *= b

print(result)

# data = input()
# result = int(data[0])
# for i in range(1,len(data)):
#     num = int(data[i])
#     if num <= 1 or result <=1:
#         result += num
#     else:
#         result *= num
# print(result)

