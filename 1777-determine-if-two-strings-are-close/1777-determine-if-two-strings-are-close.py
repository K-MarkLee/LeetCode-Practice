class Solution(object):
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False

        freq1 = {}
        freq2 = {}

        for i in word1:
            freq1[i] = freq1.get(i, 0) + 1
        
        for i in word2:
            freq2[i] = freq2.get(i, 0) + 1
        
        # freq1 = sorted([word1.count(i) for i in set(word1)])
        # freq2 = sorted([word2.count(i) for i in set(word2)])
        # return freq1 == freq2

        return sorted(freq1.values()) == sorted(freq2.values())
        