class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)

        while l <= h:
            mid = l + (h - l) // 2

            p = 1
            curr = 0
            for w in nums:
                curr += w
                if curr > mid:
                    p += 1
                    curr = w

                    if p > k:
                        break
            if p <= k:
                h = mid - 1
            else:
                l = mid + 1
        return l
