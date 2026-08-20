class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = 0
        curarr = []
        i = 0
        def dfs(currlist, i, total):
            if total > target or i >= len(nums):
                return 
            if total == target:
                ans.append(currlist.copy())
                return
            currlist.append(nums[i])
            dfs(currlist, i, total+nums[i])
            currlist.pop()
            dfs(currlist, i+1, total)

        dfs([], 0, 0)
        return ans
            

