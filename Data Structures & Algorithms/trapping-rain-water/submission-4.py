class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height)-1
        lmax = height[left]
        rmax = height[right]
        sum = 0
        while left < right:
            if lmax < rmax:
                left +=1
                lmax = max(height[left], lmax)
                sum += lmax - height[left]
            else:
                right -=1
                rmax = max(height[right], rmax)
                sum += rmax - height[right]

        return sum

        