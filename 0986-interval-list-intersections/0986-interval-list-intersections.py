class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not bool(firstList) or not bool(secondList):
            return []
        i,j=0,0
        res=[]

        while i<len(firstList) and j<len(secondList):
            s1=firstList[i][0]
            e1=firstList[i][1]
            s2=secondList[j][0]
            e2=secondList[j][1]

            s=max(s1,s2)
            e=min(e1,e2)

            if s<=e:
                res.append([s,e])
            
            if e1<=e2:
                i+=1
            else:
                j+=1
        return res
