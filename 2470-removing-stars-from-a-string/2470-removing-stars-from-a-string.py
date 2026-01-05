class Solution(object):
    def removeStars(self, s):
        result = []
        for i in s:
            if i != "*":
                result.append(i)
            else:
                result.pop()
        return "".join(result)
        