class Solution(object):
    def maxOperations(self, nums, k):
        nums = sorted(nums)
        left = result = 0
        right = len(nums)-1

        while left < right:
            sum_now = nums[left] + nums[right]
            if sum_now == k:
                result += 1
                left += 1
                right -= 1
            elif sum_now < k:
                left += 1
            else:
                right -= 1
        return result