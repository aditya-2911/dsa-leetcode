class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        size=len(nums)
        seen={0:1}
        current_sum=0
        ct=0

        for j in range(size):
            current_sum+=nums[j]
            remainder=current_sum%k
            if remainder in seen:
                ct+=seen[remainder]
            
            seen[current_sum%k] = seen.get(current_sum%k, 0) + 1


        return ct