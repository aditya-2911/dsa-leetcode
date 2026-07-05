class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ct=0
        for num in nums:

            while num>0:
                if num%10==digit:
                    ct+=1
                num//=10

        return ct