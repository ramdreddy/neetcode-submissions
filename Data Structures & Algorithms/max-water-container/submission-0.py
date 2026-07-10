class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = 0
        right = len(heights)-1
        while(left < right):
            h = min(heights[right], heights[left])
            val = (right-left)*h
            if(val > max):
                max = val
            if(heights[right] > heights[left]):
                left+=1
            else:
                right-=1
        return max
    
            
            
    

        