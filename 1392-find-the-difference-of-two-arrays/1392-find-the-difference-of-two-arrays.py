class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        result1 = [num for num in set1 if num not in set2]
        result2 = [num for num in set2 if num not in set1]
        return[result1, result2]