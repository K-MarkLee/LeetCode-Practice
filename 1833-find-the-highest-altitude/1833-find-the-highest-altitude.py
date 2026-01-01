class Solution(object):
    def largestAltitude(self, gain):
        result = 0
        now = 0
        for i in gain:
            now += i
            if now > result:
                result = now

        return result