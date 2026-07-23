class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows*cols-1
        while(l <= r):
            mid = (l + r)//2
            mc = mid%cols
            mr = mid // cols
            if target > matrix[mr][mc]:
                l = mid +1
            elif target < matrix[mr][mc]:
                r = mid - 1
            else:
                return True
        return False


        