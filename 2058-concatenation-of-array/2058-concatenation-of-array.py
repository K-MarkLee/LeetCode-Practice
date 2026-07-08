class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(2):
            for i in range(len(nums)):
                result.append(nums[i])
        return result