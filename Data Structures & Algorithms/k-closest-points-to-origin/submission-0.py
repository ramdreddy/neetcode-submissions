from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        for x,y in points:
            pdistance = (x*x+y*y)**.5
            if len(heap) == k:
                if pdistance < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, [-pdistance, x,y])
            else:
                heappush(heap, [-pdistance, x,y])
        ans = []
        while heap:
            d , x, y = heappop(heap)
            ans.append([x,y])
        return ans

                

        