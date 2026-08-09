class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        total=0
        for i,ch in enumerate(s):
            if ch==')':
                a,pop_ch=stack.pop()
                if i-a==1:
                    total+=2**len(stack)

            else:
                stack.append((i,ch))

        return total
