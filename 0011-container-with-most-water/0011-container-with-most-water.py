class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            hl = height[l]
            hr = height[r]
            if hl < hr:
                water = (r - l) * hl
                while l < r and height[l] <= hl:
                    l += 1
            else:
                water = (r - l) * hr

                while l < r and height[r] <= hr:
                    r -= 1
            maxWater = max(maxWater, water)
        return maxWater
