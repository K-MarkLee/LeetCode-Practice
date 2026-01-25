# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, root.val)]
        good = 0

        while stack:
            node, maximum = stack.pop()

            if node.val >= maximum:
                good += 1
                maximum = node.val

            if node.right:
                stack.append((node.right, max(maximum, node.right.val)))
            if node.left:
                stack.append((node.left, max(maximum, node.left.val)))

        return good