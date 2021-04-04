
data = input()
result = int(data[0]) # first integer value 5 of 567
for i in range(1,len(data)):  #if 567, i=1,2 
    num = int(data[i]) # second integer value 6 of 567 cuz i = 1
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
print(result)

#dont use list for input cuz input is just 1 single int 



    

