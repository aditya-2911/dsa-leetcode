class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curr=''
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)

            elif i=='[':
                stack.append((curr,num))
                num=0
                curr=''
            elif i==']':
                prev,n=stack.pop()
                curr=prev+(n*curr)
            else:
                curr+=i


        return curr

