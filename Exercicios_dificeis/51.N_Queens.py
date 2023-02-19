#link do exercicio
#https://leetcode.com/problems/n-queens/

class Movimentos():
    def __init__(self, numeros_rainha=4, linha=0, coluna=0):
        self.tabuleiro = {0: ["-", "-", "-", "-"],
                          1: ["-", "-", "-", "-"],
                          2: ["-", "-", "-", "-"],
                          3: ["-", "-", "-", "-"]}
        self.numeros_rainha = numeros_rainha
        self.linha_rainha = linha
        self.coluna_rainha = coluna

    def posicionarRainhas(self):
        if self.numeros_rainha == 1:
            self.tabuleiro[self.linha_rainha][self.coluna_rainha] = "T"
        else:

            self.tabuleiro[self.linha_rainha][self.coluna_rainha] = "T"
            controle.movimentoHorizontal()
            controle.movimentoVertical()
            controle.movimentoDiagonalDireitoBaixo()
            controle.movimentoDiagonalEsquerdoBaixo()
            controle.movimentoDiagonalDireitoCima()
            controle.movimentoDiagonalEsquerdoCima()

            for k, v in self.tabuleiro.items():
                for key, value in enumerate(v):
                    if self.numeros_rainha > k:
                        if self.tabuleiro[k][key] == "-":
                            self.tabuleiro[k][key] = "T"

                            self.linha_rainha = k
                            self.coluna_rainha = key
                            controle.movimentoHorizontal()
                            controle.movimentoVertical()
                            controle.movimentoDiagonalDireitoBaixo()
                            controle.movimentoDiagonalEsquerdoBaixo()
                            controle.movimentoDiagonalDireitoCima()
                            controle.movimentoDiagonalEsquerdoCima()


    def movimentoHorizontal(self):

        for k, v in enumerate(self.tabuleiro[self.linha_rainha]):
            if v != "T":
                self.tabuleiro[self.linha_rainha][k] = "0"

    def movimentoVertical(self):
        for k, v in self.tabuleiro.items():
            if self.tabuleiro[k][self.coluna_rainha] != "T":
                self.tabuleiro[k][self.coluna_rainha] = "0"

    def movimentoDiagonalDireitoBaixo(self):
        coluna_rainha = self.coluna_rainha
        for k, v in self.tabuleiro.items():
            if k > self.linha_rainha:
                coluna_rainha += 1
                try:
                    self.tabuleiro[k][coluna_rainha] = "0"

                except:
                    pass

    def movimentoDiagonalEsquerdoBaixo(self):
        coluna_rainha = self.coluna_rainha
        for k in self.tabuleiro.keys():
            if k > self.linha_rainha:
                coluna_rainha -= 1
                if coluna_rainha < 0:
                    break
                self.tabuleiro[k][coluna_rainha] = "0"

    def movimentoDiagonalDireitoCima(self):
        coluna_rainha = self.coluna_rainha
        linha_rainha = self.linha_rainha
        for k in self.tabuleiro.keys():

            if k < self.linha_rainha:

                coluna_rainha += 1
                linha_rainha -= 1
                try:
                    self.tabuleiro[linha_rainha][coluna_rainha] = "0"
                except:
                    pass

    def movimentoDiagonalEsquerdoCima(self):

        if not self.coluna_rainha == 0 or self.linha_rainha == 0:
            linha_rainha = self.linha_rainha - 1
            coluna_rainha = self.coluna_rainha - 1

            while linha_rainha >= 0 and coluna_rainha >= 0:
                self.tabuleiro[linha_rainha][coluna_rainha] = "0"
                coluna_rainha -= 1
                linha_rainha -= 1
        else:
            pass

    def exibirTabuleiro(self):
        for v in self.tabuleiro.values():
            for x in v:
                print(x, end="\t")
            print()

    def executarTodosMovimentos(self):


        controle.movimentoHorizontal()
        controle.movimentoVertical()
        controle.movimentoDiagonalDireitoBaixo()
        controle.movimentoDiagonalEsquerdoBaixo()
        controle.movimentoDiagonalDireitoCima()
        controle.movimentoDiagonalEsquerdoCima()




linha = 1
coluna = 0

controle = Movimentos(numeros_rainha=4, linha=linha, coluna=coluna)
controle.posicionarRainhas()
controle.exibirTabuleiro()
print("os '0' representam o caminho que uma rainha pode percorrer no xadrez \n"
      "e os 'T' representam as rainhas")