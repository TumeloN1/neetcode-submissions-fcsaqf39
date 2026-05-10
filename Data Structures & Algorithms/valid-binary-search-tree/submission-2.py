# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list = self.getInOrder(root)
        
        for i in range(1, len(inorder_list)):
            if inorder_list[i] <= inorder_list[i-1]:
                return False
        return True
    
    def getInOrder(self, root):
        res = []
        def backtrack(node):
            if not node:
                return
            backtrack(node.left)
            res.append(node.val)
            backtrack(node.right)
        
        backtrack(root)
        return res