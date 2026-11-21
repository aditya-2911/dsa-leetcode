class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        seen={0:1}
        prefix=0
        ct=0

        for num in nums:
            prefix+=num
            rem=prefix%k

            if rem in seen:
                ct+=seen[rem]
            else:
                seen[rem]=0

            seen[rem]+=1
        
        return ct