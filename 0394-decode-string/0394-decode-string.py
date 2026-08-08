class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        ans=''
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)

            elif i=='[':
                stack.append(num)
                num=0
            elif i==']':
                temp=''
                if stack:
                    ch=str(stack.pop())
                while not ch.isdigit():
                    temp=ch+temp
                    if stack:
                        ch=str(stack.pop())
                stack.append(temp*int(ch))
            else:
                stack.append(i)
                
        return ''.join(stack)

