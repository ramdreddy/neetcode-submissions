class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        def dfs(i, cnum, curr):
            if cnum == target:
                ans.append(curr.copy())
                return
            if cnum > target:
                return
            if i == len(nums):
                return
            curr.append(nums[i])
            dfs(i,cnum+nums[i], curr)
            curr.pop()
            dfs(i+1,cnum, curr)
        dfs(0,0,[])
        return ans

        