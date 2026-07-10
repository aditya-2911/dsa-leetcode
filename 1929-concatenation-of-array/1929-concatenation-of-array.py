class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size=len(nums)
        ans=[0]*(size*2)
        for i in range(2*size):
            ans[i]=nums[i%size]
        
        return ans