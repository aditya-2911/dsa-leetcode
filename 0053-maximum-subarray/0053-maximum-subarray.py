class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        best_end=nums[0]
        for i in range(1,len(nums)):
            best_end=max(nums[i], best_end+nums[i])
            max_sum=max(max_sum,best_end)
        return max_sum