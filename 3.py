data = input()
count0 = 0
count1 = 0

if data[0]=='1':
    count0 += 1
else:
    count1 += 1

#range explained
#if len(data) = 5 cuz data is 01100, and len-1 is range(4) which is from 0 to 3 so 0 1 2 3 is 4 iterations, just what we want
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] =='1':
            count0 +=1
        else:
            count1 +=1
print(min(count0,count1))
