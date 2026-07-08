class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size=len(nums)
        left_prod=1
        right_prod=1
        max_prod=nums[0]

        for i in range(size):
            if left_prod==0:
                left_prod=1
            if right_prod==0:
                right_prod=1
            
            left_prod*=nums[i]
            right_prod*=nums[size-1-i]

            max_prod=max(max_prod, left_prod, right_prod)

        return max_prod