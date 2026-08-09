class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for ch in s:
            if stack and ch=='B' and stack[-1]=='A':
                stack.pop()
            elif stack and ch=='D' and stack[-1]=='C':
                stack.pop()
            else:
                stack.append(ch)
        

        return len(stack)