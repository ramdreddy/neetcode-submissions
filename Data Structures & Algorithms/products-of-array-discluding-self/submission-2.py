##idea - create general product, divide by curr
## if there's a 0, you skip, if there's 2 0's just return all 0's
## store a 0 count

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        res = [] 
        p2 = 1
        for n in nums:
            if n == 0:
                count +=1
            product *= n
        if count == 1:
            for n in nums:
                if not n == 0:
                    p2*=n
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(p2)
                else:
                    res.append(0)
        elif count == 0:
            for i in range(len(nums)):
                res.append(product//nums[i])
        else:
            return [0]*(len(nums))
        return res

                    
        

        