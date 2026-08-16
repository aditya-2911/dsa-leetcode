# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue
            
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
            
        return True