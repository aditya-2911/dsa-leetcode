class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        num=n
        while n:
            d=n%10
            s+=d
            p*=d
            n//=10
        
        if num%(s+p)==0:
            return True

        return False