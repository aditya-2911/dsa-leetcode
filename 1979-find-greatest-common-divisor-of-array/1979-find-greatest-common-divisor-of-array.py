class Solution:
    def findGCD(self, nums: List[int]) -> int:

        a,b=min(nums), max(nums)

        while a!=b:
            if a>b:
                a-=b
            else:
                b-=a
        
        return a