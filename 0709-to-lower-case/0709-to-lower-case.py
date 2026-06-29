class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            if s[i].isupper():
                ans+=s[i].lower()
            else:
                ans+=s[i]
        return ans