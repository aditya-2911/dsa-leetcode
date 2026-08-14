class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size=len(nums)
        for i in range(size):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        
        prefix=[0]*(size+1)

        for i in range(1,size+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        
        ct=0
        prefix_counts={}

        for p in prefix:
            target=p-k
            if target in prefix_counts:
                ct+=prefix_counts[target]
            
            prefix_counts[p]=prefix_counts.get(p,0)+1
        
        return ct

        print(prefix)
