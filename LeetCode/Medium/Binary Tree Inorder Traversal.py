# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        sol = []
        cur = root
        while cur or len(queue) > 0:
            while cur:
                queue.append(cur)
                cur = cur.left
            cur = queue.pop()
            sol.append(cur.val)
            cur = cur.right
        return sol