class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        ans = [0]*l
        rightmax = -1
        for i in range(l-1, -1 , -1):
            ans[i] = rightmax
            rightmax = max(arr[i], rightmax)
        return ans