class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxEle=max(nums)
        moves=0
        for i in nums:
            moves+=maxEle-i
        return moves