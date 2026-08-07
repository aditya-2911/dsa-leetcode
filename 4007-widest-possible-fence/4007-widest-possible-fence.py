class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        size=len(planks)
        freq={}

        for i in planks:
            freq[i]=freq.get(i,0)+1

        unique=list(freq.keys())

        n=len(unique)

        width={}

        for i in unique:
            width[i]=width.get(i,0)+freq[i]
        for i in unique:
            width[2*i]=width.get(2*i,0)+(freq[i]//2)


    
        for i in range(n):
            for j in range(i+1,n):
                a=unique[i]
                b=unique[j]

                req=a+b

                width[req]=width.get(req,0)+min(freq[a],freq[b])


        return max(width.values()) if width else 0