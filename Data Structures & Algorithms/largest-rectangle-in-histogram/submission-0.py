class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = []
        area = 0
        c = len(heights)
        for i, h in enumerate(heights):
            p = i
            while ans and h < ans[-1][1]:
                a,b = ans.pop()
                area = max(area, b*(i-a))
                p = a
            ans.append((p,h))
        
        for x in ans:
            a,b = x
            area = max(area,(b*(c-a)))
        return area
