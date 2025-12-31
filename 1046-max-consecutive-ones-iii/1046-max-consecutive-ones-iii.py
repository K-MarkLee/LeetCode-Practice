class Solution(object):
    def longestOnes(self, nums, k):
        left = max_count = 0 

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            count = right - left + 1
            if count > max_count:
                max_count = count
        return max_count