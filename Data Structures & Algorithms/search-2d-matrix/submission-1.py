class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=(rows*cols)-1
        while left<=right:
            mid=(left+right)//2
            row=mid//cols
            col=mid%cols
            value=matrix[row][col]
            if target<value:
                right=mid-1
            elif target>value:
                left=mid+1
            elif target==value:
                return True
        return False