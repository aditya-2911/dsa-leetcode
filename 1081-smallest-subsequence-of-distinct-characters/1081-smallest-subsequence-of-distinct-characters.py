class Solution:
    def smallestSubsequence(self, s: str) -> str:
        size=len(s)
        seen=set()
        stack=[]

        last_idx={}

        for i in range(size-1,-1,-1):
            if s[i] not in last_idx:
                last_idx[s[i]]=i
        
        for i,ch in enumerate(s):
            if ch in seen:
                continue
            
            while stack and stack[-1]>ch and last_idx[stack[-1]]>i:
                seen.remove(stack.pop())
            
            stack.append(ch)
            seen.add(ch)
        
        return ''.join(stack)