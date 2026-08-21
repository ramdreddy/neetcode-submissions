from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        time = 0
        for key in count:
            heapq.heappush(heap, -count[key])
        dq = deque()
        while dq or heap:
            time+=1
            if heap:
                x = heapq.heappop(heap)
                if x+1 < 0:
                    dq.append([x+1,time+n])
            else:
                time = dq[0][1]
            if dq and time == dq[0][1]:
                y,z = dq.popleft()
                heapq.heappush(heap, y)
        return time



