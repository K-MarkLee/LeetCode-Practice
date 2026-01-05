class Solution(object):
    def asteroidCollision(self, asteroids):
        result = []
        for i in asteroids:
            while result and i < 0 < result[-1]:
                if result[-1] < -i:
                    result.pop()
                    continue
                elif result[-1] == -i:
                    result.pop()
                break
            else:
                result.append(i)
        return result