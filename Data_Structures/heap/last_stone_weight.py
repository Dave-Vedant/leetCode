import heapq

def lastStoneWeight(self, stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones)>1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first-second)  # because we are tracking negative
    
    stones.append(0)   # if stone is empty or empty during process...
    return abs(stones[0])

    # time complexity = O(Nlog(N)) --- generate heap = O(N) and pop and push operation = O(log(N)) which requrie for N times
    # space complexity = using heap to store and process O(N)
