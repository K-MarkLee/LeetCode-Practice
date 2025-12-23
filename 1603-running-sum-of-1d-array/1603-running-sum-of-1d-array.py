class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            result.append(total)

        return result