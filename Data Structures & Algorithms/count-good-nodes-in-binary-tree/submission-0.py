# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, max_so_far):
            if not node:
                return 0
            is_good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return (is_good
                    + traverse(node.left, new_max)
                    + traverse(node.right, new_max))

        return traverse(root, float("-inf"))