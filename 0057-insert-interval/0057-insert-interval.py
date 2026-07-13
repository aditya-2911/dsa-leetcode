class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def merge(intervals):
            ans = []
            for start, end in intervals:
                if not ans or ans[-1][1]<start:
                    ans.append([start, end])
                else:
                    ans[-1][1]=max(ans[-1][1], end)
            return ans

        intervals.append(newInterval)
        for i in range(len(intervals)-1,0,-1):
            if intervals[i][0]< intervals[i-1][0]:
                intervals[i],intervals[i-1]=intervals[i-1],intervals[i]
            else:
                break
        
        return merge(intervals)

        