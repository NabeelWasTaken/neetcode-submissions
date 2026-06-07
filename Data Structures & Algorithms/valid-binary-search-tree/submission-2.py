# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, right, left):

            if not root:
                return True
            
            if not (root.val < right and root.val > left):
                return False
            
            return dfs(root.right, right, root.val) and dfs(root.left, root.val, left)

        return dfs(root, float("inf"), -float("inf"))
