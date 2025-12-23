class Solution(object):
    def mergeAlternately(self, word1, word2):

        result = []
        word1_len = len(word1)
        word2_len = len(word2)
        max_len = max(word1_len, word2_len)

        for i in range(max_len):
            if i < word1_len:
                result.append(word1[i])
            if i < word2_len:
                result.append(word2[i])

        return ''.join(result)
