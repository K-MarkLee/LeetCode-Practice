class Solution(object):
    def goodNodes(self, root):
        stack = [(root, root.val)]
        good = 0

        while stack:
            node, maximum = stack.pop()

            if node.val >= maximum:
                good += 1
            
            maximum = max(maximum, node.val)

            if node.right:
                stack.append((node.right, maximum))
            if node.left:
                stack.append((node.left, maximum))

        return good