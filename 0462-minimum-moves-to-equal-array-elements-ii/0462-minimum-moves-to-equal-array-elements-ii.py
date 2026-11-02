class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        l,r=0,n-1

        while l<r:
            ans+=nums[r]-nums[l]
            l+=1
            r-=1
        return ans