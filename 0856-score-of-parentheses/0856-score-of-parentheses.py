class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]

        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(0)
            else:
                inner=stack.pop()

                curr=max(2*inner,1)

                stack[-1]+=curr


        return stack[-1]
