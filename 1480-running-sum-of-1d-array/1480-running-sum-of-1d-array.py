class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prefix=[0]*size
        prefix[0]=nums[0]
        for i in range(1,size):
            prefix[i]=prefix[i-1]+nums[i]
        
        return prefix