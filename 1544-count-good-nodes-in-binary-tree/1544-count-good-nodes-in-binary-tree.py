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

            if node.right:
                stack.append((node.right, max(maximum, node.val)))
            if node.left:
                stack.append((node.left, max(maximum, node.val)))

        return good