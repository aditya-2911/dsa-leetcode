class Solution:
    def minimumPushes(self, word: str) -> int:
        cost=1

        used=0
        ans=0

        for ch in word:
            ans+=cost
            used+=1
            if used==8:
                cost+=1
                used=0
        return ans