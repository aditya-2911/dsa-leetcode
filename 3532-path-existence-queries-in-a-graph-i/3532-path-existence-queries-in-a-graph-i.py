class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        component_id=0
        component=[0]*len(nums)
    
        for i in range(1,len(nums)):
            if abs(nums[i]-nums[i-1]) > maxDiff:
                component_id+=1
            
            component[i]=component_id

        res=[]

        for query in queries:
            u,v=query[0],query[1]
            res.append(component[u]==component[v])

        return res