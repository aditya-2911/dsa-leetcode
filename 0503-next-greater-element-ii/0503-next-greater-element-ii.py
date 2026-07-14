class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [-1] * size
        stack = []

        for i in range(size - 2, -1, -1):
            stack.append(nums[i])


        for i in range(size - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])

        return ans
