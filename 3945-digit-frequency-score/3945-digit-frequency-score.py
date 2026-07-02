class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n=str(n)
        score=0
        for i in n:
            score+= int(i)
    
        return score