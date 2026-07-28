class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        for i in s:
            freq[ord(i) - 97] += 1

        left = []
        middle = ""

        for i in range(26):
            f = freq[i]
            if f:
                ch = chr(i + 97)
                left.append(ch * (f // 2))
                if f & 1:
                    middle = ch

        left = "".join(left)
        return left + middle + left[::-1]
