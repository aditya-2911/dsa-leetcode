class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        sum_val=0
        i=1
        while n>0:
            d=n%10
            if d!= 0:
                sum_val+=d
                x = d*i + x
                i=i*10
            n//=10
            
        print(x,sum_val)
        return x*sum_val
            
                
