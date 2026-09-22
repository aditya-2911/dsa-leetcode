class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        n_pow = 1
        while n_pow < n:
            n_pow *= 2
            
        tree_tot = [1] * (2 * n_pow)
        tree_cnt = [[0] * k for _ in range(2 * n_pow)]
        
        for i in range(n):
            idx = n_pow + i
            val = nums[i] % k
            tree_tot[idx] = val
            tree_cnt[idx][val] = 1
            
        for i in range(n_pow - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            
            tree_tot[i] = (tree_tot[left] * tree_tot[right]) % k
            
            for j in range(k):
                tree_cnt[i][j] = tree_cnt[left][j]
                
            ltot = tree_tot[left]
            for j in range(k):
                if tree_cnt[right][j]:
                    tree_cnt[i][(ltot * j) % k] += tree_cnt[right][j]
                    
        ans = []
        
        for index, value, start, x in queries:
            idx = n_pow + index
            val = value % k
            
            tree_tot[idx] = val
            for j in range(k):
                tree_cnt[idx][j] = 0
            tree_cnt[idx][val] = 1
            
            idx //= 2
            while idx > 0:
                left = 2 * idx
                right = 2 * idx + 1
                
                tree_tot[idx] = (tree_tot[left] * tree_tot[right]) % k
                
                for j in range(k):
                    tree_cnt[idx][j] = tree_cnt[left][j]
                    
                ltot = tree_tot[left]
                for j in range(k):
                    if tree_cnt[right][j]:
                        tree_cnt[idx][(ltot * j) % k] += tree_cnt[right][j]
                        
                idx //= 2
                
            L = start + n_pow
            R = (n - 1) + n_pow
            
            left_nodes = []
            right_nodes = []
            
            while L <= R:
                if L % 2 == 1:
                    left_nodes.append(L)
                    L += 1
                if R % 2 == 0:
                    right_nodes.append(R)
                    R -= 1
                L //= 2
                R //= 2
                
            res_tot = 1
            res_cnt = [0] * k
            
            for node in left_nodes:
                ntot = tree_tot[node]
                ncnt = tree_cnt[node]
                for j in range(k):
                    if ncnt[j]:
                        res_cnt[(res_tot * j) % k] += ncnt[j]
                res_tot = (res_tot * ntot) % k
                
            for node in reversed(right_nodes):
                ntot = tree_tot[node]
                ncnt = tree_cnt[node]
                for j in range(k):
                    if ncnt[j]:
                        res_cnt[(res_tot * j) % k] += ncnt[j]
                res_tot = (res_tot * ntot) % k
                
            ans.append(res_cnt[x])
            
        return ans