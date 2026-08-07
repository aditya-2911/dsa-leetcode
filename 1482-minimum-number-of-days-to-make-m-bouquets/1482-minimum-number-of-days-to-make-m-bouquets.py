class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        size=len(bloomDay)
        if size<m*k:
            return -1
        l=1
        h=max(bloomDay)

        while l<=h:
            day=l+(h-l)//2

            bouquets=0
            flower=0
            for d in bloomDay:
                if d<=day:
                    flower+=1
                    if flower==k:
                        bouquets+=1
                        flower=0
                        if bouquets==m:
                            break
                else:
                    flower=0
            
            if bouquets>=m:
                ans=day
                h=day-1
            else:
                l=day+1
        return ans
                
                