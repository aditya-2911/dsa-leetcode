import heapq
from collections import defaultdict

class Solution:
    def minOperations(self,nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        INF = float('inf')

        lo = []
        hi = []  
        delayed = defaultdict(int)
        lo_size = hi_size = 0
        sum_lo = sum_hi = 0

        def prune(h, is_lo):
            while h:
                v = -h[0] if is_lo else h[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heapq.heappop(h)
                else:
                    break

        def balance():
            nonlocal lo_size, hi_size, sum_lo, sum_hi
            if lo_size > hi_size + 1:
                prune(lo, True)
                v = -heapq.heappop(lo)
                heapq.heappush(hi, v)
                lo_size -= 1; hi_size += 1
                sum_lo -= v; sum_hi += v
                prune(lo, True)
            elif lo_size < hi_size:
                prune(hi, False)
                v = heapq.heappop(hi)
                heapq.heappush(lo, -v)
                hi_size -= 1; lo_size += 1
                sum_hi -= v; sum_lo += v
                prune(hi, False)

        def add(v):
            nonlocal lo_size, hi_size, sum_lo, sum_hi
            prune(lo, True)
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v); lo_size += 1; sum_lo += v
            else:
                heapq.heappush(hi, v); hi_size += 1; sum_hi += v
            balance()

        def remove(v):
            nonlocal lo_size, hi_size, sum_lo, sum_hi
            prune(lo, True)
            delayed[v] += 1
            if lo and v <= -lo[0]:
                lo_size -= 1; sum_lo -= v
                if v == -lo[0]:
                    prune(lo, True)
            else:
                hi_size -= 1; sum_hi -= v
                if hi and v == hi[0]:
                    prune(hi, False)
            balance()

        cost = []
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                prune(lo, True)
                med = -lo[0]
                cost.append(med * lo_size - sum_lo + sum_hi - med * hi_size)

        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] < INF:
                    cur[i] = min(cur[i], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]