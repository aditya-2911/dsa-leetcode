class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l=1
        h=position[-1]-position[0]
        ans=h

        while l<=h:
            force=l+(h-l)//2

            balls=1
            curr=position[0]
            for pos in position:
                if pos-curr>=force:
                    balls+=1
                    curr=pos

                    if balls==m:
                        break
            if balls>=m:
                ans=force
                l=force+1
            else:
                h=force-1
        
        return ans
            