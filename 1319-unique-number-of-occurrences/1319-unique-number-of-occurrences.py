class Solution(object):
    def uniqueOccurrences(self, arr):
        result = {}

        for i in arr:
            result[i] = result.get(i, 0) + 1

        # setarr = set()
        # for i in result.values():
        #     if i in setarr:
        #         return False
        #     setarr.add(i)
        # return True
        
        values = result.values()
        return len(values) == len(set(values))