class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD=10**9+7

        temp=nums

        ct0,ct1=0,0
        swap=0

        for i in range(len(nums)-1,-1,-1):
            if nums[i]<a:
                ct0+=1
            elif nums[i]<=b:
                swap=(swap+ct0)%MOD
                ct1+=1
            else:
                swap=(swap+ct0+ct1)%MOD

        return swap