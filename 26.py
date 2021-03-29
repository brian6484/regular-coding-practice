import heapq

n = int(input())

heap =[]
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result=0
while len(heap)!= 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum = one +two
    result += sum
    heapq.heappush(heap,sum)
    #no need reset value of 1,2,sum cuz while loop does it automatically
    one, two, sum = 0,0,0

print(result)