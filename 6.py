import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1

    q =[]
    for i in range(len(food_times)):
        #(우선 순위, 값)
        heapq.heappush(q,(food_times[i], i+1))
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0]-previous)*length) <=k:
        now = heapq.heappop(q)[0]

food_times = [2,3,2]
print(solution)
        