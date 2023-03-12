#link do exercicio:
#https://leetcode.com/problems/valid-parentheses/
s = '() {} []'

class Solution:
    def validaString(self, s: str) -> bool:
        self.s = s
        self.caracteres = ["()", "[]", "{}"]

        for k, v in enumerate(self.s):
            if len(self.s) == 1:
                return False
            else:
                try:
                    if self.s[k] + self.s[k + 1] in self.caracteres:
                        return True
                    else:
                        return False
                except:
                    pass


solution = Solution()

print(solution.validaString(s))
