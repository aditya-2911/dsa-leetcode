class Solution:
    class SegmentTree:
        def __init__(self, n: int):
            self.n = n
            self.sum_val = [0] * (4 * n)
            self.sum_sq = [0] * (4 * n)
            self.lazy = [0] * (4 * n)
            self.MOD = 10**9 + 7

        def _apply(self, node: int, l: int, r: int, val: int):
            length = r - l + 1
            v = val % self.MOD
            
            self.sum_sq[node] = (self.sum_sq[node] + 2 * v * self.sum_val[node] + v * v * length) % self.MOD
            self.sum_val[node] = (self.sum_val[node] + v * length) % self.MOD
            self.lazy[node] = (self.lazy[node] + v) % self.MOD

        def _push(self, node: int, l: int, r: int):
            if self.lazy[node] != 0:
                mid = (l + r) // 2
                self._apply(2 * node, l, mid, self.lazy[node])
                self._apply(2 * node + 1, mid + 1, r, self.lazy[node])
                self.lazy[node] = 0

        def update(self, node: int, l: int, r: int, ql: int, qr: int, val: int):
            if ql <= l and r <= qr:
                self._apply(node, l, r, val)
                return
            
            self._push(node, l, r)
            mid = (l + r) // 2
            
            if ql <= mid:
                self.update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                self.update(2 * node + 1, mid + 1, r, ql, qr, val)
                
            self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD
            self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD


    def sumCounts(self,nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        st = self.SegmentTree(n)
        last_pos = {}
        total_ans = 0

        for j in range(n):
            x = nums[j]
            prev_idx = last_pos.get(x, -1)
            
            st.update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            total_ans = (total_ans + st.sum_sq[1]) % MOD
            
            last_pos[x] = j

        return total_ans