/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int maxDepth;
    public int maxDepth(TreeNode root) {
        
        if (root == null){
            return 0;
        }
        int a = maxDepth(root.right);
        int b = maxDepth(root.left);


        return 1 + Math.max(a,b);
    }

}
