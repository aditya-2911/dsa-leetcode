class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n=len(s)
        freq = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in s:
            freq[i]=freq.get(i,0)+1
        
        def backtrack(index: int) -> str:
            if index == len(target):
                return ""
            
            t_char = target[index]
        
            if freq[t_char] > 0:
                freq[t_char] -= 1
                
                future_string = backtrack(index + 1)
                if future_string != "":
                    return t_char + future_string

                freq[t_char] += 1 

            for char_code in range(ord(t_char) + 1, ord('z') + 1):
                char = chr(char_code)
                if freq[char] > 0:
                    freq[char] -= 1
                    
                    remainder = []
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        remainder.append(c * freq[c])
                        
                    return char + "".join(remainder)
            
            return ""

        return backtrack(0)
        