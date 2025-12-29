class Solution(object):
    def maxArea(self, height):
        l = result = 0
        r = len(height) - 1

        while l < r:
            if height[l] < height[r]:
                water = height[l] * (r - l)
                result = max(water, result)
                l += 1
            else:
                water = height[r] * (r - l)
                result = max(water, result)
                r -= 1
        return result