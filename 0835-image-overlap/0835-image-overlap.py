class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        from collections import Counter
        n = len(img1)
        ones_img1 = []
        ones_img2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones_img1.append((r, c))
                if img2[r][c] == 1:
                    ones_img2.append((r, c))
                    
        vector_counts = Counter()
        
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                vector = (r2 - r1, c2 - c1)
                vector_counts[vector] += 1
                
        return max(vector_counts.values()) if vector_counts else 0