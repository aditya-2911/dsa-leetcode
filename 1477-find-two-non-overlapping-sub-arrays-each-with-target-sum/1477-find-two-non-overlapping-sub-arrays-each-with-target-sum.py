class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n 
        
        ans = float('inf')
        best_single_len = float('inf')
        
        left = 0
        window_sum = 0
        
        for right in range(n):
            window_sum += arr[right]
            while window_sum > target and left <= right:
                window_sum -= arr[left]
                left += 1
                
            if window_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])

                best_single_len = min(best_single_len, curr_len)
            
            min_len[right] = best_single_len
            
        return ans if ans != float('inf') else -1