# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.ans=0

        def dfs(node):
            if node is None:
                return float('-inf')
            max_l=dfs(node.left)
            max_r=dfs(node.right)

            subtree_max= max(node.val,max_l,max_r)

            if node.val==subtree_max:
                self.ans+=1

            return subtree_max

        dfs(root)
        return self.ans