import sys
sys.setrecursionlimit(200005)
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 18
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        def dfs(v, p, d):
            nonlocal timer
            timer += 1
            tin[v] = timer
            up[v][0] = p
            depth[v] = d
            
            for i in range(1, LOG):
                up[v][i] = up[up[v][i-1]][i-1]
                
            for to in adj[v]:
                if to != p:
                    dfs(to, v, d + 1)
                    
            tout[v] = timer
            
        dfs(0, 0, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
            
        bit = [0] * (n + 2)
        def update_bit(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        chars = list(s)
        
        for i in range(n):
            val = 1 << (ord(chars[i]) - 97)

            update_bit(tin[i], val)
            update_bit(tout[i] + 1, val)
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                if chars[u] != c:
                    old_val = 1 << (ord(chars[u]) - 97)
                    new_val = 1 << (ord(c) - 97)
                    diff = old_val ^ new_val
                    update_bit(tin[u], diff)
                    update_bit(tout[u] + 1, diff)
                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = query_bit(tin[u])
                mask_v = query_bit(tin[v])
                mask_lca = 1 << (ord(chars[lca]) - 97)
                
                path_mask = mask_u ^ mask_v ^ mask_lca
                
                if path_mask & (path_mask - 1) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans