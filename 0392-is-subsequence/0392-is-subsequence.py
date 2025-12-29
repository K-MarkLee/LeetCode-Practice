class Solution(object):
    def isSubsequence(self, s, t):
        checked = 0
        
        for char in t:
            if checked < len(s) and char == s[checked]:
                checked += 1
        
        return checked == len(s)
        