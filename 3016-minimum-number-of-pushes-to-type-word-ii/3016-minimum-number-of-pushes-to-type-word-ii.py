class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        press = 0
        total_cost = 0
        for val in freq.values():
            total_cost += (press // 8 + 1) * val
            press += 1

        return total_cost
