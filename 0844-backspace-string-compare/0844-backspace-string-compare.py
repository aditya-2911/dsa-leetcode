class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]

        for i in s:
            if stack1 and i=='#':
                stack1.pop()
            elif i!='#':
                stack1.append(i)
        for i in t:
            if stack2 and i=='#':
                stack2.pop()
            elif i!='#':
                    stack2.append(i)
        
        s=''
        while stack1:
            s+=stack1.pop()
        t=''
        while stack2:
            t+=stack2.pop()

        return s==t
        