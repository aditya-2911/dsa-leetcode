import math
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []

        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
                    
        ans = 0
        
        for k in divisors:
            possible = True
            prev_max = float('-inf')
            
            for i in range(0, n, k):
                drops = 0
                drop_idx = -1
                
                for j in range(k - 1):
                    if nums[i + j] > nums[i + j + 1]:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            break
                            
                if drops > 1:
                    possible = False
                    break

                if drops == 0:
                    chunk_min = nums[i]
                    chunk_max = nums[i + k - 1]
                elif drops == 1:
                    if nums[i + k - 1] <= nums[i]:
                        chunk_max = nums[i + drop_idx]
                        chunk_min = nums[i + drop_idx + 1]
                    else:
                        possible = False
                        break

                if chunk_min < prev_max:
                    possible = False
                    break
                prev_max = chunk_max

            if possible:
                ans += k
                
        return ans