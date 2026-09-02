class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        ct = 0
        def is_pal(l,r):
            while r > l:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        while right > left:
            if s[left] != s[right]:
                return is_pal(left+1,right) or is_pal(left, right-1)
            left+=1
            right-=1
            
        return True
        
