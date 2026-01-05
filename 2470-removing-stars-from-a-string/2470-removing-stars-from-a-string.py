class Solution(object):
    def removeStars(self, s):
        result = []
        for i in s:
            if i == "*":
                result.pop()
            else:
                result.append(i)
        return "".join(result)
        