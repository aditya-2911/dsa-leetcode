class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        i,j=0,2*len(nums)-1
        ans=[0]*(2*len(nums))
        while i<j:
            for num in nums:
                ans[i]=num
                ans[j]=num
                i+=1
                j-=1
        return ans