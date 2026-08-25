class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        candidates.sort()
        def dfs(i, csum, arr):
            if csum == target:
                res.append(arr.copy())
                return
            if i == len(candidates) or csum > target:
                return
            arr.append(candidates[i])
            dfs(i+1, csum + candidates[i], arr)
            arr.pop()
            while(i < len(candidates)-1 and candidates[i] == candidates[i+1]):
                i+=1
            dfs(i+1, csum, arr)
        dfs(0, 0, [])
        return res

            
            