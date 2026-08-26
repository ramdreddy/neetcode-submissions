class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        ans = []
        while left <= right:
            r = nums[right]
            l = nums[left]
            if r*r > l*l:
                ans.append(r*r)
                right-=1
            else:
                ans.append(l*l)
                left+=1
        return ans[::-1]


        