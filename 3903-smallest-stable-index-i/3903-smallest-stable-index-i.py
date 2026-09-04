class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        

        suffix=[0]*n
        suffix[n-1]=nums[n-1]

        for i in range(n-2,-1,-1):
            suffix[i]=min(nums[i],suffix[i+1])
        max_ele=nums[0]

        for i in range(n):
            max_ele=max(max_ele,nums[i])
            if max_ele-suffix[i]<=k:
                return i

        return -1