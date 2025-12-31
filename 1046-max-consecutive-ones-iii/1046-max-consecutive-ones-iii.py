class Solution(object):
    def longestOnes(self, nums, k):
        count = left = max_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            max_count = max(max_count, right - left + 1)
        return max_count


        