class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = -1
        ans=0
        for i in nums:
            if i == 0:
                curr=0

            else:
                max_digit, min_digit =0,9
                num = i
                while num > 0:
                    d = num % 10
                    if d > max_digit:
                        max_digit = d
                    if d < min_digit:
                        min_digit = d
                    num //= 10

                curr=max_digit-min_digit

            if curr>max_range:
                max_range=curr
                ans=i
            elif curr==max_range:
                ans+=i

        return ans

        
 
