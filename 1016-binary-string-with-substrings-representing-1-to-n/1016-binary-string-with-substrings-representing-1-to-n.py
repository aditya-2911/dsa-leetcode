class Solution:
    import math
    def queryString(self, s: str, n: int) -> bool:
        if n > 2000:
            return False
        freq=set()
        b=s.encode('ascii')

        for i in range(len(b)):
            if b[i]==48:
                continue
            num=0

            for j in range(i,min(i+30, len(b))):
                num= (num<<1)| (b[j] & 1)
                if 1<=num<=n:
                    freq.add(num)
                    if len(freq)==n: return True
        return len(freq)==n
        

