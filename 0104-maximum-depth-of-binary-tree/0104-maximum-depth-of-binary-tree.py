# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = 0
        stack = [root]

        if not root:
            return depth

        while stack:
            level = len(stack)
            depth += 1

            for i in range(level):
                node = stack.pop(0)

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return depth