import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        heapq.heapify(self.arr)
        self.leng = k
        while len(nums) > k:
            heapq.heappop(self.arr)

    def add(self, val: int) -> int:
        if len(self.arr) < self.leng:
            heapq.heappush(self.arr, val)
            return self.arr[0]
        elif val > self.arr[0]:
            heapq.heappop(self.arr)
            heapq.heappush(self.arr, val)
            return self.arr[0]
        else:
            return self.arr[0]
            
            

        
