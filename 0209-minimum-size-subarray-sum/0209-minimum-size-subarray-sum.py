class Solution:
    def findMaxFrequency(self, arr):
        maxCount = float("-inf")
        for i in arr:
            if i >= maxCount:
                maxCount = i
        return maxCount

    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        low = 0
        maxLength = float("-inf")

        for high in range(0, len(s)):
            index = ord(s[high]) % 65
            freq[index] += 1
            maxCount = self.findMaxFrequency(freq)
            currentLength = high - low + 1
            difference = currentLength - maxCount

            while difference > k:
                freq[ord(s[low]) % 65] -= 1
                low += 1
                maxCount = self.findMaxFrequency(freq)
                currentLength = high - low + 1
                difference = currentLength - maxCount

            currentLength = high - low + 1
            maxLength = max(maxLength, currentLength)

        return maxLength
