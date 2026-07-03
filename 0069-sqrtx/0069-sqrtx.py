import math
class Solution:
    def mySqrt(self, n: int) -> int:
        e = 0.000001
        x = n / 2
        y = 0

        while abs(x-y)>e:
            y=n/x
            x=(x+y)/2
        
        return math.floor(x)