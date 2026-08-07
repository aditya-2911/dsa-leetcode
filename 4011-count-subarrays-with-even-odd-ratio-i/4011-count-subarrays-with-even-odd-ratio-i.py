class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        size=len(nums)
        valid=0

        for i in range(size):
            x=0
            y=0

            for j in range(i,size):
                if not nums[j]&1:
                    x+=1
                else:
                    y+=1

                if y>0 and (x*b)<=(a*y):
                    valid+=1

        return valid
