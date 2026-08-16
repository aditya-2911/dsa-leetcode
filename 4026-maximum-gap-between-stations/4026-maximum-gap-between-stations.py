class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n=len(skill)
        m=len(station)

        if n<=1:
            return 0
            
        L=[0]*n
        w=0
        for s in range(m):
            if w<n and skill[w]==station[s]:
                L[w]=s
                w+=1
        R=[0]*n
        w=n-1
        for s in range(m-1,-1,-1):
            if w>=0 and skill[w]==station[s]:
                R[w]=s
                w-=1

        maxGap=0

        for i in range(1,n):
            maxGap=max(maxGap, R[i]-L[i-1])

        return maxGap
        