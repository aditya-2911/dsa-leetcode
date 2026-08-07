class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ct_0=0
        ct_1=0
        res=0
        for i in s:
            if i=='0':
                ct_0+=1
            else:
                ct_1+=1

            if abs(ct_0-ct_1)<2:
                res+=1
        return res