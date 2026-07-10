class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            target = -nums[i]
            left = i +1
            right = len(nums)-1
            while(right > left):
                if nums[right]+nums[left] > target:
                    right-=1
                elif nums[right]+nums[left] < target:
                    left+=1
                else:
                    ans.append([nums[i],nums[right],nums[left]])
                    left+=1
                    while(left < right and nums[left]==nums[left-1] ):
                        left+=1
                        
        return ans
                

        