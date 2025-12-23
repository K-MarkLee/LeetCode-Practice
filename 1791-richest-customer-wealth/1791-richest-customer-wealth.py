class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = []

        for account in accounts:
            result.append(sum(account))
        
        return max(result)