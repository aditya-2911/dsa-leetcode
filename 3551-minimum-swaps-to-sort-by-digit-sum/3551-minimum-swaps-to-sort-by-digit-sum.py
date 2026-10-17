class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)

        indexed_nums = []
        for idx, val in enumerate(nums):
            indexed_nums.append(((digit_sum(val), val), idx))

        indexed_nums.sort()
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexed_nums[i][1] == i:
                visited[i] = True
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][1]
                cycle_size += 1

            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps
