# link do exercicio
# https://leetcode.com/problems/n-queens/
print('=' * 70)
print("os '0' representam o caminho que uma rainha pode percorrer no xadrez \n"
      "e os 'T' representam as rainhas")
print('=' * 70)


class Movimentos():
    def __init__(self, numeros_rainha, linha, coluna):

        self.tabuleiro = {0: ["-", "-", "-", "-"],
                          1: ["-", "-", "-", "-"],
                          2: ["-", "-", "-", "-"],
                          3: ["-", "-", "-", "-"]}

        self.numeros_rainha = numeros_rainha
        self.linha_rainha = linha
        self.coluna_rainha = coluna
        self.rainha = "\033[31mT\033[m"

    def posicionarRainhas(self) -> list[list[str]]:
        self.tabuleiro[self.linha_rainha][self.coluna_rainha] = self.rainha
        controle.movimentoHorizontal()
        controle.movimentoVertical()
        controle.movimentoDiagonalDireitoBaixo()
        controle.movimentoDiagonalEsquerdoBaixo()
        controle.movimentoDiagonalDireitoCima()
        controle.movimentoDiagonalEsquerdoCima()
        self.numeros_rainha -= 1

        for k, v in self.tabuleiro.items():
            for key, value in enumerate(v):
                if self.numeros_rainha == 0:
                    break

                if self.tabuleiro[k][key] == "-":
                    self.numeros_rainha -= 1
                    self.tabuleiro[k][key] = self.rainha

                    self.linha_rainha = k
                    self.coluna_rainha = key
                    controle.movimentoHorizontal()
                    controle.movimentoVertical()
                    controle.movimentoDiagonalDireitoBaixo()
                    controle.movimentoDiagonalEsquerdoBaixo()
                    controle.movimentoDiagonalDireitoCima()
                    controle.movimentoDiagonalEsquerdoCima()
        valores = []
        for v in self.tabuleiro.values():
            valores.append(v)

        return valores

    def movimentoHorizontal(self):

        for k, v in enumerate(self.tabuleiro[self.linha_rainha]):
            if v != self.rainha:
                self.tabuleiro[self.linha_rainha][k] = "0"

    def movimentoVertical(self):
        for k, v in self.tabuleiro.items():
            if self.tabuleiro[k][self.coluna_rainha] != self.rainha:
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

    def contarrainhas(self):
        numeros_rainhas = 0
        for v in self.tabuleiro.values():
            numeros_rainhas += v.count(self.rainha)
        return numeros_rainhas

    def pegartabuleiro(self):
        return self.tabuleiro


def exibirTabuleiro(tabuleiro: list[dict[int, list[str]]]) -> None:
    for value in tabuleiro:
        for v in value.values():
            for letra in v:
                print(letra, end='\t')
            print()
        print("=" * 14)


def eliminaTabuleiroRepetido(tabuleiros: list[dict[int, list[str]]]) -> list[dict[int, list[str]]]:
    count = 0
    for value in tabuleiros:
        count = tabuleiros.count(value)
        while count > 1:
            tabuleiros.remove(value)
            count -= 1
    return tabuleiros


def possibilidades():
    coluna = 0
    linha = 0
    tabuleiros = []
    numero_rainha = int(input("Quantas rainhas deseja posicionar: "))
    if numero_rainha == 1:
        return 1
    while linha != 3:
        global controle
        controle = Movimentos(numeros_rainha=numero_rainha, linha=linha, coluna=coluna)

        controle.posicionarRainhas()
        if controle.contarrainhas() == numero_rainha:
            tabuleiros.append(controle.pegartabuleiro())

        coluna += 1
        if coluna > 3:
            coluna = 0
            if linha != 3:
                linha += 1
    tabuleiros = eliminaTabuleiroRepetido(tabuleiros)
    exibirTabuleiro(tabuleiros)


possibilidades()
