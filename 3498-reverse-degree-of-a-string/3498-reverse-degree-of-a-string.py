class Solution:
    def reverseDegree(self, s: str) -> int:
        deg=0

        for i,c in enumerate(s):
            deg+=(i+1)*(26-(ord(c)-97))
    
        return deg