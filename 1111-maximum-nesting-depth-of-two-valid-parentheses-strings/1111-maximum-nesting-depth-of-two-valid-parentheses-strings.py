class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans=[]
        mem=0
        for i in seq:
            if i=='(':
                ans.append(mem%2)
                mem+=1
                
            else:
                mem-=1
                ans.append(mem%2)

        return ans