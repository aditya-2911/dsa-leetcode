class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        ans = [0] * size
        stack = []

        for i in range(size - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans
