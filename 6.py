import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1

    q =[]
    for i in range(len(food_times)):
        #(food time, food index)
        heapq.heappush(q,(food_times[i], i+1))
    #time taken to eat
    sum_value = 0

    #time taken for eat just now
    previous = 0
    length = len(food_times)

    # no need reset q[0][0] with ij cuz heappop resets it by kicking it out 
    while sum_value + ((q[0][0]-previous)*length) <=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1
        previous = now
    
    result = sorted(q, key = lambda x:x[1])
    return result[(k-sum_value)%length][1]


        