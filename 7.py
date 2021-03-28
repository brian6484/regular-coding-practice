data = input()
ans = 0
mid = len(data)//2

sum0 = 0
sum1 = 0
for i in range(mid):
    sum0 += int(data[i])
for i in range(mid,len(data)):
    sum1 += int(data[i])
if sum0!=sum1:
    print("ready")
else:
    print("lucky")


# for i in range(len(data)//2):
#     ans += int(data[i])
# for i in range(len(data)//2,len(data)):
#     ans -= int(data[i])

# if ans == 0:
#     print("lucky")
# else:
#     print("ready")

