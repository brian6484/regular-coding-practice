data = input()
ans = 0
for i in range(len(data)//2):
    ans += int(data[i])
for i in range(len(data)//2,len(data)):
    ans -= int(data[i])

if ans == 0:
    print("lucky")
else:
    print("ready")

