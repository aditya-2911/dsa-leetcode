class Solution:
    import math
    def queryString(self, s: str, n: int) -> bool:
        if n > 2000:
            return False
        freq=set()
        for i in range(len(s)):
            if s[i]=='0':
                continue
            num=0

            for j in range(i,min(i+30, len(s))):
                num= (num<<1)+int(s[j])
                if 1<=num<=n:
                    freq.add(num)
                    if len(freq)==n: return True
        return len(freq)==n
        

