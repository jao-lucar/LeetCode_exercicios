#link do exercício:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def __init__(self, string: str):
        self.string = string

    def lengthOfLongestSubstring(self):
        todos_iguais = True
        for v in self.string:
            if self.string[0] == v:
                continue
            else:
                todos_iguais = False

        if todos_iguais:
            return len(self.string[0:1])



        sub_strings = []
        while len(self.string) != 0:
            index_auxiliar = 1
            index_auxiliar2 = 0
            for v in self.string:

                if self.string[index_auxiliar:index_auxiliar + 1] not in self.string[index_auxiliar2:index_auxiliar]:
                    sub_strings.append(self.string[index_auxiliar2:index_auxiliar + 1])
                else:
                    break

                index_auxiliar += 1
            self.string = self.string.removeprefix(self.string[0])

        maior = 0
        for v in sub_strings:
            if len(v) > maior:
                maior = len(v)

        return maior


a = 'pwwkew'
y = Solution(a)
x = y.lengthOfLongestSubstring()
print(x)
