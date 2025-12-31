class Solution(object):
    def longestOnes(self, nums, k):
        left = result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            if result < (right - left + 1):
                result = right - left + 1
        return result