class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n=len(skill)
        m=len(station)

        if n<=1:
            return 0
            
        L=[0]*n
        w=0
        for i,s in enumerate(station):
            if w<n and skill[w]==s:
                L[w]=i
                w+=1

        w=n-1
        maxGap=0
        for s in range(m-1,-1,-1):
            if w>0 and skill[w]==station[s]:
                maxGap=max(maxGap, s-L[w-1])
                w-=1

        return maxGap
        