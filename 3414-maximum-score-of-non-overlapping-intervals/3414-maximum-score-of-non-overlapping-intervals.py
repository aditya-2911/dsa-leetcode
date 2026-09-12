class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        n = len(intervals)
        pairs = []
        for i, (l, r, w) in enumerate(intervals):
            pairs.append((l, r, w, i))
            
        pairs.sort(key=lambda x: x[0])
        
        starts = [p[0] for p in pairs]
    
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            l, r, w, original_idx = pairs[i]
            next_i = bisect.bisect_right(starts, r)
            
            for k in range(1, 5):
                skip_score, skip_list = dp[i + 1][k]
                
                take_score_prev, take_list_prev = dp[next_i][k - 1]
                take_score = w + take_score_prev
                take_list = sorted([original_idx] + take_list_prev)
                
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_list)
                elif skip_score > take_score:
                    dp[i][k] = (skip_score, skip_list)
                else:
                    dp[i][k] = (take_score, min(take_list, skip_list))
                    
        return dp[0][4][1]