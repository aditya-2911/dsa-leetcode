class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        for i in text:
            freq[i]=freq.get(i,0)+1
        


        ans = min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )

        return ans