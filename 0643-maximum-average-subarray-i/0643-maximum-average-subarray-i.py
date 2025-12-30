class Solution(object):
    def findMaxAverage(self, nums, k):
        first = sum(nums[:k])
        result = first
        
        for i in range(k,len(nums)):
            first += nums[i] - nums[i-k]
            result = max(result, first)
        return result / float(k)
