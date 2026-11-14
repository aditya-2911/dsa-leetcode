class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        pre=[0]*(n+1)

        for i in range(n):
            pre[i+1]=pre[i]+nums[i]
        
        ans=float('inf')

        for i in range(n):
            for j in range(i+l,min(n,i+r)+1):
                curr_sum=pre[j]-pre[i]
                if curr_sum>0:
                    ans=min(ans,curr_sum)
        if ans!=float('inf'):
            return ans
        else:
            return -1