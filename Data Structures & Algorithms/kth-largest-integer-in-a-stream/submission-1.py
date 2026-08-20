from heapq import *
class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.largest = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)


    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.largest:
            heappop(self.heap)
        return self.heap[0]
