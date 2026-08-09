class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ct=0
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    ct+=1
        
        return len(stack)+ct