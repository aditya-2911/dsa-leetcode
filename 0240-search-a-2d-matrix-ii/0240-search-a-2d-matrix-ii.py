class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        for row in matrix:
            if row[n-1]>=target:
                l,r=0,n-1

                while l<=r:
                    mid=l+(r-l)//2

                    if row[mid]==target: return True
                    elif row[mid]<target: l=mid+1
                    else: r=mid-1

        return False