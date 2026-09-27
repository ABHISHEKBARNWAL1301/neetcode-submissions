# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            def height(root):
                if root:
                    if root in dp:
                        return dp[root]
                    dp[root] =  1 + max(height(root.left), height(root.right))
                    return dp[root]
                return 0

            dp = {}
            return max(
                height(root.left) + height(root.right), 
                max(
                    self.diameterOfBinaryTree(root.left), 
                    self.diameterOfBinaryTree(root.right)
                    )
                )
        return 0