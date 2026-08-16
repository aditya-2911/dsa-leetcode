# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        queue=deque()
        queue.append((p,q))
        
        while queue:
            node1,node2=queue.popleft()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            
            queue.append((node1.left,node2.left))
            queue.append((node1.right,node2.right))

        return True