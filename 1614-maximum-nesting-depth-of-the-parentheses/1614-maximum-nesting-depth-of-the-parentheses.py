class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth=0
        curr=0
        for i in s:
            if i =='(':
                curr+=1
            elif i==')':
                curr-=1
            maxDepth=max(curr,maxDepth)
        return maxDepth