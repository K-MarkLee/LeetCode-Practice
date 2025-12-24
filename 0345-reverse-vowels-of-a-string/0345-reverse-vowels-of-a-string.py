class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = ['a','e','i','o','u']

        left, right = 0, len(s_list)-1

        while left < right:
            while left < right and lower(s_list[left]) not in vowels:
                left += 1
            while left < right and lower(s_list[right]) not in vowels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]

            left += 1
            right -= 1

        return "".join(s_list)
