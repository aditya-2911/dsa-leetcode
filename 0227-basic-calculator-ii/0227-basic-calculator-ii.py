class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        op='+'
        num=0

        for ch in s+'+':

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
        
        return sum(stack)
        