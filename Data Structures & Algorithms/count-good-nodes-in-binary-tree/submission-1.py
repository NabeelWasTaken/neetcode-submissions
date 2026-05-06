# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxVal):

            if not root:
                return 0

            
            if root.val >= maxVal:
                res = 1
            else:
                res = 0

            
            maxVal = max(root.val, maxVal)
            left = dfs(root.left, maxVal)
            right = dfs(root.right, maxVal)
            return res+left+right

        
        return dfs(root, root.val)
        

