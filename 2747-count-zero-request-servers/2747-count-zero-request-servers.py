class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda log:log[1])

        sorted_queries=sorted([(q,i) for i,q in enumerate (queries)])

        ans=[0]*len(queries)
        ct={}
        unique_servers=0
        l,r=0,0

        for time,idx in sorted_queries:
            while r<len(logs) and logs[r][1]<=time:
                server_id=logs[r][0]
                ct[server_id]=ct.get(server_id,0)+1

                if ct[server_id]==1:
                    unique_servers+=1
                r+=1
            
            while l<r and logs[l][1]<time-x:
                server_id=logs[l][0]

                ct[server_id]-=1
                if ct[server_id]==0:
                    unique_servers-=1
                l+=1
            
            ans[idx]=n-unique_servers
        
        return ans