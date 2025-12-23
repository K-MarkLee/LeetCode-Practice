class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        result = []
        for i in range(len(candies)):
            n = candies[i] + extraCandies
            if n >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
        