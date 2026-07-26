class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        after=''
        ans=''
        for i in s:
            if i==x:
                after+=i
            else:
                ans+=i

        return ans+after