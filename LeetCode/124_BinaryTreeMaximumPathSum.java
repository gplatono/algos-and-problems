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
    
    private int[] maxPathDFS(TreeNode node) {
        if (node.left == null && node.right == null) {
            return new int[]{node.val, node.val};
        }
        
        int leftMaxPath, leftContPath, rightMaxPath, rightContPath;
        leftMaxPath = leftContPath = rightMaxPath = rightContPath = -1000000000;
        if (node.left != null) {
            int[] left = maxPathDFS(node.left);
            leftMaxPath = left[0];
            leftContPath = left[1];
        }
        if (node.right != null) {
            int[] right = maxPathDFS(node.right);
            rightMaxPath = right[0];
            rightContPath = right[1];
        }
        
        int thisContPath = Integer.max(node.val, Integer.max(node.val + leftContPath, node.val + rightContPath));
        int maxChildPath = Integer.max(leftMaxPath, rightMaxPath);
        
        int thisMaxPath = Integer.max(thisContPath, maxChildPath);
        if (node.val + leftContPath + rightContPath > thisMaxPath)
             thisMaxPath = node.val + leftContPath + rightContPath;
        
        return new int[]{thisMaxPath, thisContPath};
    }
    
    public int maxPathSum(TreeNode root) {
        int[] maxPath = maxPathDFS(root);
        return maxPath[0];
    }
}