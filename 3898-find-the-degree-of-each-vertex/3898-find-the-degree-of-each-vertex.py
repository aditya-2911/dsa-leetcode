class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[]

        for vertex in matrix:
            s=0
            for edge in vertex:
                s+=edge
            res.append(s)

        return res
        