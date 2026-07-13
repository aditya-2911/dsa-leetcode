class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans=[]
        i=0
        size=len(intervals)

        while i<size and newInterval[0]>intervals[i][1]:
            ans.append(intervals[i])
            i+=1
        
        while i<size and newInterval[1]>=intervals[i][0]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        ans.append(newInterval)

        while i<size:
            ans.append(intervals[i])
            i+=1
        return ans
