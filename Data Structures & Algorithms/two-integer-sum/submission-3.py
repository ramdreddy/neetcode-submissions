class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## keep a hash which stores needed number, if you find needed number, return
        checker = {}
        for i in range(len(nums)):
            if nums[i] in checker:
                return [checker[nums[i]],i]
            else:
                checker[target - nums[i]] = i
        

        