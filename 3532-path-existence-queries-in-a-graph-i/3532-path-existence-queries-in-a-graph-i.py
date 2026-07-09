class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        component_id=0
        component=[0]*n
    
        for i in range(1,n):
            if nums[i]-nums[i-1] > maxDiff:
                component_id+=1
            
            component[i]=component_id

        return [component[u] == component[v] for u, v in queries]