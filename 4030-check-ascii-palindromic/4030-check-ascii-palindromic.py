class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin_str=''
        lst=[]
        for i in s:
            lst.append(f'{ord(i):08b}')
        
        bin_str=''.join(lst)

        l,r=0,len(bin_str)-1

        while l<r:
            if bin_str[l]!=bin_str[r]:
                return False
            l+=1
            r-=1
        
        return True