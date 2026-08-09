class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]

        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            
            stack.append(i)
        while k:
            if stack:
                stack.pop()
            k-=1
        ans=''.join(stack)

        res=ans.lstrip('0')

        return res if res else '0'