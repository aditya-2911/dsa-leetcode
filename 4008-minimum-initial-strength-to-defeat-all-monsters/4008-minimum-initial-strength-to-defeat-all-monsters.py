class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        size=len(monsters)
        bonus=[0]*(size+1)

        for b in boosts:
            bonus[b[0]]+=b[2]
            bonus[b[1]+1]-=b[2]

        prefix=[0]*size
        curr=0

        for i in range(size):
            curr+=bonus[i]
            prefix[i]=curr


        req=0

        for i in range(size-1,-1,-1):
            if req>0:
                req+=monsters[i]
            else:
                req=max(0,monsters[i]-prefix[i])

        return req