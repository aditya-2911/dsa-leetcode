class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans=[]
        for row in range(m):
            if row==0:
                temp='.' * n
                ans.append(temp)
            else:
                temp1='#'*(n-1)
                temp1+='.'
                ans.append(temp1)
        return ans