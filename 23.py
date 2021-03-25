t = int(input())
array = []

for i in range(t):
    data = input().split()
    # care brackets, i put 1,2 brackets and cant cuz
    # need to format into 1 argument
    #also line 9 or line 10 is same
    # array.append((data[0],int(data[1])))
    array.append(data)

array = sorted(array, key = lambda x:x[1])
print(array)

# t = int(input())
# array = []

# for i in range(t):
#     data = input().split()
#     array.append(data)

# array = sorted(array, key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
# print(array)

