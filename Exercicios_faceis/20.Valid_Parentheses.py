#link do exercicio:
#https://leetcode.com/problems/valid-parentheses/
s = '[](){}'

class Solution:
    def validaString(self, s: str) -> bool:
        self.s = s
        self.caracteres = ["()", "[]", "{}"]

        for k in enumerate(self.s):
            try:
                if self.s[k[0]] + self.s[k[0] + 1] in self.caracteres:
                    return True
                else:
                    return False
            except:
                pass


solution = Solution()

print(solution.validaString(s))
