class Solution(object):
    def maxArea(self, height):
        left = result = 0
        right = len(height) - 1

        while left < right:
            w = right - left
            h = min(height[right], height[left])

            result = max(w*h,result)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result