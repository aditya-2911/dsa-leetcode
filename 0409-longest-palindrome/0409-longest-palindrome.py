class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        odd = False
        length = 0

        for value in freq.values():
            if value & 1:
                length += value - 1
                odd = True
            else:
                length += value
        if odd:
            length += 1
        return length
