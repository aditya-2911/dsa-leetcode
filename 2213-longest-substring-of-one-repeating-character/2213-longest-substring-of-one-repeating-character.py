class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)

        tree_size = 4 * n + 4
        
        max_l = [0] * tree_size
        pre_l = [0] * tree_size
        suf_l = [0] * tree_size
        pre_c = [''] * tree_size
        suf_c = [''] * tree_size
        
        s_list = list(s)

        def build(p: int, start: int, end: int):
            if start == end:
                char = s_list[start]
                max_l[p] = pre_l[p] = suf_l[p] = 1
                pre_c[p] = suf_c[p] = char
                return
                
            mid = (start + end) // 2
            left = 2 * p
            right = 2 * p + 1
            
            build(left, start, mid)
            build(right, mid + 1, end)
            
            sz_left = mid - start + 1
            sz_right = end - mid
            
            pre_c[p] = pre_c[left]
            suf_c[p] = suf_c[right]
            
            pre_l[p] = pre_l[left]
            if pre_l[left] == sz_left and pre_c[left] == pre_c[right]:
                pre_l[p] += pre_l[right]
                
            suf_l[p] = suf_l[right]
            if suf_l[right] == sz_right and suf_c[right] == suf_c[left]:
                suf_l[p] += suf_l[left]
                
            m1 = max_l[left]
            m2 = max_l[right]
            best = m1 if m1 > m2 else m2
            
            if suf_c[left] == pre_c[right]:
                cross_len = suf_l[left] + pre_l[right]
                if cross_len > best:
                    best = cross_len
                    
            max_l[p] = best

        def update(p: int, start: int, end: int, idx: int, char: str):
            if start == end:
                pre_c[p] = suf_c[p] = char
                return
                
            mid = (start + end) // 2
            left = 2 * p
            right = 2 * p + 1
            
            if idx <= mid:
                update(left, start, mid, idx, char)
            else:
                update(right, mid + 1, end, idx, char)
                
            sz_left = mid - start + 1
            sz_right = end - mid
            
            pre_c[p] = pre_c[left]
            suf_c[p] = suf_c[right]
            
            pre_l[p] = pre_l[left]
            if pre_l[left] == sz_left and pre_c[left] == pre_c[right]:
                pre_l[p] += pre_l[right]
                
            suf_l[p] = suf_l[right]
            if suf_l[right] == sz_right and suf_c[right] == suf_c[left]:
                suf_l[p] += suf_l[left]
                
            m1 = max_l[left]
            m2 = max_l[right]
            best = m1 if m1 > m2 else m2
            
            if suf_c[left] == pre_c[right]:
                cross_len = suf_l[left] + pre_l[right]
                if cross_len > best:
                    best = cross_len
                    
            max_l[p] = best

        build(1, 0, n - 1)
        
        ans = []
        for idx, char in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, idx, char)
            ans.append(max_l[1])
            
        return ans