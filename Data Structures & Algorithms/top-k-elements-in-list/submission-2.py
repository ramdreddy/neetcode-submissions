### idea - make hash for each
### bucket sort - 
### 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for n in nums:
            if n in mp:
                mp[n]+=1
            else:
                mp[n] = 1
        counter = [[] for i in range(len(nums)+1)]
        for l in mp:
            counter[mp[l]].append(l)
        i = len(counter)-1
        while i > 0:
            for x in counter[i]:
                res.append(x)
                if len(res) == k:
                    return res
            i-=1
        return res
                



        