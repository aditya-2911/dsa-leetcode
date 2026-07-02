class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n=str(n)
        freq={}
        for i in n:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        score=0
        for key, value in freq.items():
            score+= (int(key)*value)
    
        return score