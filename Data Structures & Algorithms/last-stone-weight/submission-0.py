from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if x != y:
                heappush(heap,  x - y)
        if heap:
            return -heap[0]
        else:
            return 0
