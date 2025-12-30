class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left = result = 0
        right = len(nums)-1

        while left < right:
            if nums[left] + nums[right] == k:
                result += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return result