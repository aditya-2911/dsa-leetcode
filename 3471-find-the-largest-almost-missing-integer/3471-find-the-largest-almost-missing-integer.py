class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        size=len(nums)
        if k == size:
            return max(nums)

        freq={}
        max_num_with_1_freq=-1

        for i in nums:
            freq[i]=freq.get(i,0)+1

        if k==1:
            for key,val in freq.items():
                if val==1:
                    max_num_with_1_freq=max(max_num_with_1_freq,key)
    
            return max_num_with_1_freq
        
        if k==size:
            return max_num

        
        ans=-1
        n1=nums[0]
        if freq[n1]==1:
            ans=max(ans,n1)

        n2=nums[size-1]
        if freq[n2]==1:
            ans=max(ans,n2)
        
        return ans

            
