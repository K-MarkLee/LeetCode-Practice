class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for i in nums:
            if first >= i:
                first = i
            elif second >= i:
                second = i
            else:
                return True
        return False