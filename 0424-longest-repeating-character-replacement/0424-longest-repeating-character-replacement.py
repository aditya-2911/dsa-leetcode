class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        maxCount = 0
        low = 0

        for high in range(len(s)):
            index = ord(s[high]) - 65
            freq[index] += 1

            if freq[index] > maxCount:
                maxCount = freq[index]

            if (high - low + 1) - maxCount > k:
                freq[ord(s[low]) - 65] -= 1

                low += 1
        return high - low + 1
