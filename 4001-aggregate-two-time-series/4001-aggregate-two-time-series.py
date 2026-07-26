class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        n1,n2=len(series1),len(series2)
        ans=[]

        i,j=0,0

        while i<n1 and j<n2:
            if series1[i][0] < series2[j][0]:
                ans.append([series1[i][0], series1[i][1], None])
                i+=1
            elif series1[i][0] > series2[j][0]:
                ans.append([series2[j][0], None,series2[j][1]])
                j+=1
            else:
                ans.append([series1[i][0], series1[i][1],series2[j][1]])
                i+=1
                j+=1

        while i<n1:
            ans.append([series1[i][0], series1[i][1], None])
            i+=1
        while j<n2:
            ans.append([series2[j][0],None, series2[j][1]])
            j+=1

        res=[]
        next1=next2=0
        for k in range(len(ans)-1,-1,-1):
            item=ans[k]
            if item[1] is not None:
                next1=item[1]
            if item[2] is not None:
                next2=item[2]

            res.append([item[0], next1+next2])

        res.reverse()
            
        return res

    