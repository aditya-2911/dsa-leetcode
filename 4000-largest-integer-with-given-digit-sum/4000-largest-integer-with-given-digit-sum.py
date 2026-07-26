class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if 9*n<s:
            return -1
        if s==0:
            return 0
        ans=0
        for _ in range(n):
            d=min(9,s)
            ans=ans*10+d
            s-=d

        return ans