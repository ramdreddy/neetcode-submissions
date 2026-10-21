import heapq
##idea - have a min heap with the k largest elements
## have a max heap with the rest
## if a new element is less than the current min of the largest, push it into the max
## else if its greater, pop the curr head and push
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.leng = k
        self.minheap = []
        for n in nums:
            heapq.heappush(self.minheap, n)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        if len(self.minheap) < self.leng:
            heapq.heappush(self.minheap, val)
        elif val > self.minheap[0]:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
        return self.minheap[0]

        
