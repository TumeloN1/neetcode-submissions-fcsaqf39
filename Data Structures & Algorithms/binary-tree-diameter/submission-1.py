# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxlength = 0
        length = self.diameter(root)
        return self.maxlength

    def diameter(self, root):
        if not root:
            return -1
        left = 1 + self.diameter(root.left)
        right = 1 + self.diameter(root.right)

        self.maxlength = max(self.maxlength, left + right)

        return max(left, right)

        