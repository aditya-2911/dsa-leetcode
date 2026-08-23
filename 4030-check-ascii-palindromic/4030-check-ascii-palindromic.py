class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin_str=''

        for i in s:
            bin_str+=f'{ord(i):08b}'

        l,r=0,len(bin_str)-1
        print(bin_str)
        while l<r:
            if bin_str[l]!=bin_str[r]:
                return False
            l+=1
            r-=1
        
        return True