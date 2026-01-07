class Solution(object):
    def decodeString(self, s):
        result = []
        for i in s:
            if i != "]":
                result.append(i)
            else:
                char = []
                while result[-1] != "[":
                    char.append(result.pop())
                char.reverse()
                result.pop()

                str_num = ''
                while result and result[-1].isdigit():
                    str_num = result.pop() + str_num
                num = int(str_num)if str_num else 1
                temp = ''.join(char) * num
                for i in temp:
                    result.append(i)
        return ''.join(result)