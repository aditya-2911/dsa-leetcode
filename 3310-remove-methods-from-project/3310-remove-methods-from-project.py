class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]

        for u,v in invocations:
            graph[u].append(v)
        
        sus=[False]*n

        def dfs(u):
            sus[u]=True
            for v in graph[u]:
                if not sus[v]:
                    dfs(v)
        
        dfs(k)

        for u,v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))
        
        ans=[]

        for i in range(n):
            if not sus[i]:
                ans.append(i)
        
        return ans