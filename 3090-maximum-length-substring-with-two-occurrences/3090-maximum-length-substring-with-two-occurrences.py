class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        
        l=0
        maxLen=0

        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1

            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1
            
            maxLen=max(maxLen,r-l+1)

        return maxLen
