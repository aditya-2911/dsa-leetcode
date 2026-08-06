class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)

        ans=h

        while l<=h:
            mid=l+(h-l)//2

            d=1
            curr=0
            for w in weights:
                if curr+w>mid:
                    d+=1
                    curr=w
                else:
                    curr+=w
            if d<=days:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans