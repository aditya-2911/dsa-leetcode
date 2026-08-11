class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        
        return self.power(x,n,1)
    
    def power(self,x,n,ans):
        if n==0:
            return ans
        if n&1:
            ans*=x
        
        return self.power(x*x,n//2,ans)
            