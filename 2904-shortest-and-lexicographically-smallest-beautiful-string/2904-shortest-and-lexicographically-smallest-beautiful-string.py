class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        ones=0

        for i in s:
            if i=='1':
                ones+=1
        if ones<k:
            return ''
        
        l=0
        ones=0
        min_len=101
        ans=''
        for r in range(n):
            if s[r]=='1':
                ones+=1

            while ones>k or (ones==k and s[l]=='0'):
                if s[l]=='1':
                    ones-=1
                l+=1
            
            
            if ones==k:
                curr_len=r-l+1
                if curr_len<min_len:
                    ans=s[l:r+1]
                    min_len=curr_len
                elif curr_len==min_len:
                    if s[l:r+1]<ans:
                        ans=s[l:r+1]

        return ans