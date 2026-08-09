class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return '0'

        stack=[]

        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            
            stack.append(i)
        
        ans=''.join(stack)

        res=ans.lstrip('0')
        if k:
            res=res[:-k]

        return res if res else '0'