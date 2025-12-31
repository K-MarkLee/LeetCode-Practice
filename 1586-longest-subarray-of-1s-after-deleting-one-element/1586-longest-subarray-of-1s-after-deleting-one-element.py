class Solution(object):
    def longestSubarray(self, nums):
        left = result = count =  0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1

            max_count = right - left
            if max_count > result:
                result = max_count
        return result
        