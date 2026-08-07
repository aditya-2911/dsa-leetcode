import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
                
        if temp > 1:
            return "-1"

        memo = {}
        
        def get_min_suffix(R: int) -> str:
            if R == 1:
                return ""
            if R in memo:
                return memo[R]
            
            best = None
            for d in range(2, 10):
                g = math.gcd(R, d)
                if g > 1:
                    sub = get_min_suffix(R // g)
                    if sub is not None:
                        cand = "".join(sorted(sub + str(d)))
                        if best is None:
                            best = cand
                        elif len(cand) < len(best):
                            best = cand
                        elif len(cand) == len(best) and cand < best:
                            best = cand
                            
            memo[R] = best
            return best

        N = len(num)
        
        z = N
        for i in range(N):
            if num[i] == '0':
                z = i
                break
                
        rem_t = [t] * (N + 1)
        for i in range(N):
            d = int(num[i])
            if d == 0:
                break
            rem_t[i+1] = rem_t[i] // math.gcd(rem_t[i], d)
            
        for i in range(min(N, z), -1, -1):
            R_prefix = rem_t[i]
            
            if i == N:
                if R_prefix == 1 and z == N:
                    return num
                continue
                
            start_d = max(1, int(num[i]) + 1)
            for d in range(start_d, 10):
                R_new = R_prefix // math.gcd(R_prefix, d)
                L = N - 1 - i
                
                req_suffix = get_min_suffix(R_new)
                
                if req_suffix is not None and len(req_suffix) <= L:
                    pad = "1" * (L - len(req_suffix))
                    return num[:i] + str(d) + pad + req_suffix
                    
        req_suffix = get_min_suffix(t)
        L = max(N + 1, len(req_suffix))
        pad = "1" * (L - len(req_suffix))
        
        return pad + req_suffix