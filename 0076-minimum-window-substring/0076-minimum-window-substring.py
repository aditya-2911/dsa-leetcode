class Solution:
    def func(self,freq_s,freq_t)->bool:
        for key,value in freq_t.items():
            if key in freq_s and freq_s[key]>=value:
                continue
            else:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        freq_t=dict()
        for i in t:
            if i in freq_t:
                freq_t[i]+=1
            else:
                freq_t[i]=1
        
        freq_s={}
        low=0
        start=0
        minLen=float('inf')
        for high in range(len(s)):
            if s[high] in freq_s:
                freq_s[s[high]]+=1
            else:
                freq_s[s[high]]=1
            
            while self.func(freq_s,freq_t):
                length=high-low+1

                if length<minLen:
                    minLen=length
                    start=low
                
                freq_s[s[low]]-=1
                if freq_s[s[low]]==0:
                    del freq_s[s[low]]
                low+=1
        return s[start:start+minLen] if minLen != float('inf') else ""
