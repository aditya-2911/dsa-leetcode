class Solution:
    def calculate(self, s: str) -> int:
        size=len(s)
        stack=[]
        op='+'
        num=0

        for i in range(size+1):
            if i<size:
                ch=s[i]
            else:
                ch='+'

            if ch.isdigit():
                num=num*10+int(ch)
            elif ch!=' ':
                if (op=='+'):
                    stack.append(num)
                elif op=='-':
                    stack.append(-num)
                elif op=='*':
                    stack.append(stack.pop()*num)
                elif op=='/':
                    stack.append(int(stack.pop()/num))
                op=ch
                num=0
        print(stack)
        ans=0
        while stack:
            ans+=stack.pop()
        
        return ans
        