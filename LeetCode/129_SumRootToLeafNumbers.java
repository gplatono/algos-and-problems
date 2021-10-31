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
    
    private int sumDFS(TreeNode node, int sumSoFar) {
        sumSoFar = sumSoFar*10 + node.val;
        if (node.left == null && node.right == null)
            return sumSoFar;
        
        int childSum = 0;
        if (node.left != null)
            childSum += sumDFS(node.left, sumSoFar);
        if (node.right != null)
            childSum += sumDFS(node.right, sumSoFar);
        
        return childSum;
    }
    public int sumNumbers(TreeNode root) {
        return sumDFS(root, 0);
    }
}