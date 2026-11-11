class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        i=0
        j=1
        ans=[0]*n

        for num in nums:
            if num<0:
                ans[j]=num
                j+=2
            else:
                ans[i]=num
                i+=2
        return ans
