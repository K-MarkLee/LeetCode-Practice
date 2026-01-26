# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix = {0:1}

        def dfs(root, current_sum):
            if not root:
                return 0

            current_sum += root.val
            count = prefix.get(current_sum - targetSum, 0)
            prefix[current_sum] = prefix.get(current_sum, 0) + 1
            count += dfs(root.left, current_sum) + dfs(root.right, current_sum)
            prefix[current_sum] -= 1

            return count
        
        return dfs(root, 0)