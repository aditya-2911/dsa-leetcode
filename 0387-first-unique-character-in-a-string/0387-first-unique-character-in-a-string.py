class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i,c in enumerate(s):
            if c in freq:
                freq[c]=-1
            else:
                freq[c]=i
        ans=float('inf')
        for val in freq.values():
            if val!=-1:
                ans=min(ans, val)
        
        return ans if ans!=float('inf') else -1
            