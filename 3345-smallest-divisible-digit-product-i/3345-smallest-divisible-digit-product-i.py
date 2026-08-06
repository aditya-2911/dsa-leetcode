class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(num):
            prod=1

            while num:
                prod*=num%10
                num//=10
            return prod
        
        while True:
            p=product(n)
            if p%t==0:
                return n
            n+=1