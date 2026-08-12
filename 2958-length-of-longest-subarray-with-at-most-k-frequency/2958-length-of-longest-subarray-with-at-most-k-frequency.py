class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        size=len(nums)
        l=0
        freq={}
        maxLen=0

        for r in range(size):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1

            maxLen=max(maxLen,r-l+1)
        
        return maxLen