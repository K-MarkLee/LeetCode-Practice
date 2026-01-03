class Solution(object):
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False
        
        freq1 = sorted([word1.count(i) for i in set(word1)])
        freq2 = sorted([word2.count(i) for i in set(word2)])
        return freq1 == freq2


        