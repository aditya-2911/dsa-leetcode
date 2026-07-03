class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = [0] * 128
        required = 0
        
        for i in t:
            idx = ord(i)
            if freq_t[idx] == 0:
                required += 1
            freq_t[idx] += 1
        filtered_s = []
        for i in range(len(s)):
            if freq_t[ord(s[i])] > 0:
                filtered_s.append((i, ord(s[i])))

        freq_s = [0] * 128
        has = 0
        
        low = 0
        start = 0
        minLen = float('inf')

        for high in range(len(filtered_s)):
            curr_idx, char_code = filtered_s[high]
            freq_s[char_code] += 1
            
            if freq_s[char_code] == freq_t[char_code]:
                has += 1

            while has == required:
                left_idx, left_code = filtered_s[low]
                
                length = curr_idx - left_idx + 1
                if length < minLen:
                    minLen = length
                    start = left_idx
                freq_s[left_code] -= 1
                
                if freq_s[left_code] < freq_t[left_code]:
                    has -= 1
                    
                low += 1
                
        return s[start:start+minLen] if minLen != float('inf') else ""