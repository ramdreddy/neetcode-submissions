##so first heapify stones, then while there's 2 left, 
## pop 2, do the thing, push it back

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x == y:
                continue
            elif y > x:
                heapq.heappush(stones, -(y - x))
        if stones:
            return -stones[0]
        else:
            return 0
            
            

        