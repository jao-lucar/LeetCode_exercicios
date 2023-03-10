#link do exercício: https://leetcode.com/problems/add-two-numbers/
class Solution:
    def __init__(self, lista1: list, lista2: list):
        self.lista1 = lista1
        self.lista2 = lista2

    def addTwoNumbers(self):
        lista_auxiliar1 = []
        lista_auxiliar2 = []
        juntar_lista1 = ''
        juntar_lista2 = ''
        resultado = []

        for k, v in enumerate(self.lista1):
            v = str(v)
            lista_auxiliar1.insert(-k, v)

        for k, v in enumerate(self.lista2):
            v = str(v)
            lista_auxiliar2.insert(-k, v)

        resultador_auxiliar = str((int(juntar_lista1.join(lista_auxiliar1)) + int(juntar_lista2.join(lista_auxiliar2))))
        for v in resultador_auxiliar:
            resultado.append(int(v))
        resultado = resultado[::-1]
        return resultado


solution = Solution([2, 4, 3], [5, 6, 4])
x = solution.addTwoNumbers()
print(x)
