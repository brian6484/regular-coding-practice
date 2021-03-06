# t = int(input())
# array = list(map(int,input().split()))
# for i in range(t):
#     if array[i] == i:
#         print(i)

def binary_search(array,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array,start,mid-1)
    else:
        return binary_search(array,start,mid+1)

