class Solution(object):
    def reverseWords(self, s):
        s_split = s.split()
        s_split.reverse()
        
        return " ".join(s_split)
        