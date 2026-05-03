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
    public boolean isBalanced(TreeNode root) {

        return dfs(root)[0] == 1;
        
    }

    private int[] dfs(TreeNode root){

        if (root == null){
            return new int[] {1,0};
        }

        int[] right = dfs(root.right);
        int[] left = dfs(root.left);

        boolean condition = (Math.abs(right[1] - left[1]) <= 1 && left[0] == 1 && right[0] == 1);
        int cond = 0;

        if (condition == true){
            cond = 1;
        }
        if (condition == false){
            cond = 0;
        }

        return new int[]{cond,1 + Math.max(right[1],left[1])};

        

    }
}
