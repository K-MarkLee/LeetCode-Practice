class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counts = [0] * 26

        for char in magazine:
            counts[ord(char) - ord('a')] += 1

        for char in ransomNote:
            index = ord(char) - ord('a')

            if counts[index] == 0:
                return False
            
            counts[index] -= 1

        return True