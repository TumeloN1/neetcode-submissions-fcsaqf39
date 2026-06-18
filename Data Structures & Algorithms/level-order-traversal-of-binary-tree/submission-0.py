# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        level order traversal as a list of lists
        we can use bfs here, this gives us values based on dist from the root
        from left to right
        once we reach the end of a level, we make a new list
        """
        if not root:
            return []
        levelOrder = []
        q = collections.deque([root])
        while q:
            size = len(q)
            level = []
            for i in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level.append(curr.val)
            levelOrder.append(level)

        return levelOrder


        