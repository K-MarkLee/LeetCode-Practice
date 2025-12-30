class Solution(object):
    def maxVowels(self, s, k):
        count = max_count = 0
        vowels = set("aeiou")

        for i in s[:k]:
            if i in vowels:
                count += 1
        
        max_count = count
        if count == k:
            return k
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            
            if count > max_count:
                max_count = count
                if count == k:
                    return k
                    
        return max_count 