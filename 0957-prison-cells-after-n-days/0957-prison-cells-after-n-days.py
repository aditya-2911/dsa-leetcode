class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen={}

        while n>0:
            state=tuple(cells)
            if state in seen:
                cycleLen=seen[state]-n
                n%=cycleLen

                if n==0:
                    break
                seen.clear()
            else:
                seen[state]=n
            
            if n>0:
                next_day=[0]*8
                for i in range(1,7):
                    next_day[i]=cells[i-1]^cells[i+1]^1

                cells=next_day
                n-=1
        return cells