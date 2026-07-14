class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(0, len(s)):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i], 1])
        
        ans=''
        for c, ct in stack:
            ans+=c*ct

        return ans
