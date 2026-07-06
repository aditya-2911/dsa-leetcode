class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ct=0
        seen=set()
        for i in range(0,len(intervals)):
            for j in range(i+1,len(intervals)):
                if (intervals[i][0]>=intervals[j][0] and intervals[i][1]<=intervals[j][1]):
                    if i not in seen:
                        seen.add(i)
                        ct+=1

                elif(intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]):
                    if j not in seen:
                        seen.add(j)
                        ct+=1
        
        return len(intervals)-ct
