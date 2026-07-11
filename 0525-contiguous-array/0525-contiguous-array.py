class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        size=len(nums)
        preSum=0
        seen={0:-1}
        maxLen=0

        for i in range(size):
            if nums[i]==0:
                preSum+= -1
            else:
                preSum+=1
            

            if preSum in seen:
                l=i-seen[preSum]
                if l>maxLen:
                    maxLen=l
            else:
                seen[preSum]=i
        
        return maxLen
