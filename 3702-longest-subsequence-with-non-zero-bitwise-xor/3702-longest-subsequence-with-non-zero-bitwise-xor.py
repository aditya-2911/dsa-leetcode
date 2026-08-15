class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        size=len(nums)

        if sum(nums)==0:
            return 0

        xor=nums[0]
        for i in range(1,size):
            xor=xor^nums[i]
        
        if xor==0:
            return size-1
        else:
            return size