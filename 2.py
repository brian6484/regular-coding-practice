
data = input()
result = int(data[0])
for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
print(result)

#dont use list for input cuz input is just 1 single int 



    

