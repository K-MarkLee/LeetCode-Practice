# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def getLeaves(root):
            stack = [root]
            leaves = []
            if not stack:
                return leaves

            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leaves.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            
            return leaves
        
        tree1 = getLeaves(root1)
        tree2 = getLeaves(root2)
        return tree1 == tree2