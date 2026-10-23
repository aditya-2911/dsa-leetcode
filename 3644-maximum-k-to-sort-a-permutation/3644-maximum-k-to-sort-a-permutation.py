class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        k=-1

        for i in range(n):
            if i != nums[i]:
                if k==-1:
                    k=nums[i]
                else:
                    k=k & nums[i]
        
        return 0 if k==-1 else k