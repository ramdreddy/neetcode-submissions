##idea
##map linking key to count
##go through map and find 2 biggest counts

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        ans = []
        for n in nums:
            if n in m:
                m[n]+=1
            else:
                m[n]=1
        bucket = [[] for i in range(len(nums) + 1)]
        for x in m:
            p1 = m[x]
            bucket[p1].append(x)
        i = len(nums)
        while i > 0:
            for y in bucket[i]:
                ans.append(y)
                if len(ans) == k:
                    return ans
            i-=1
        return ans
                


            

            



        