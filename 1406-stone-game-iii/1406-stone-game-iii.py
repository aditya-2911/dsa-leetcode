class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        size=len(stones)

        dp1,dp2,dp3=0,0,0

        for i in range(size-1,-1,-1):
            take=stones[i]
            diff=take-dp1

            if i+1<size:
                take+=stones[i+1]
                diff=max(diff,take-dp2)
            
            if i+2<size:
                take+=stones[i+2]
                diff=max(diff,take-dp3)
            
            dp3=dp2
            dp2=dp1
            dp1=diff
        
        if dp1>0:
            return 'Alice'
        elif dp1<0:
            return 'Bob'
        else:
            return 'Tie'