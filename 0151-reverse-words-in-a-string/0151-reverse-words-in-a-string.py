class Solution(object):
    def reverseWords(self, s):
        s_split = s.split()[::-1]
        return " ".join(s_split)