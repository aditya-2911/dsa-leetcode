class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen=set(nums)

        max_sum= nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                break
            
            max_sum+=nums[i]
        
        while True:
            if max_sum not in nums:
                return max_sum
            max_sum+=1



        
