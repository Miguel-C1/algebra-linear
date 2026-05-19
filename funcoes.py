def imprimir_matriz(matriz):
    for linha in matriz:
        print(["{:.2f}".format(valor) for valor in linha])
    print()


def trocar_linhas(matriz, i, j):
    matriz[i], matriz[j] = matriz[j], matriz[i]


def multiplicar_linha(matriz, i, escalar):
    matriz[i] = [valor * escalar for valor in matriz[i]]


def somar_linhas(matriz, origem, destino, escalar):
    matriz[destino] = [
        matriz[destino][k] + escalar * matriz[origem][k]
        for k in range(len(matriz[0]))
    ]


def triangularizar(matriz):
    n = len(matriz)
    trocas = 0

    for coluna in range(n):

        if matriz[coluna][coluna] == 0:
            for linha in range(coluna + 1, n):
                if matriz[linha][coluna] != 0:
                    trocar_linhas(matriz, coluna, linha)
                    trocas += 1
                    break

        pivo = matriz[coluna][coluna]

        if pivo == 0:
            continue

        for linha in range(coluna + 1, n):
            fator = -matriz[linha][coluna] / pivo
            somar_linhas(matriz, coluna, linha, fator)

    return matriz, trocas

def determinante_matriz_triangular(matriz, trocas=0):
    determinante = 1

    for i in range(len(matriz)):
        determinante *= matriz[i][i]

    if trocas % 2 != 0:
        determinante *= -1

    return determinante

def retrosubstituicao(matriz):
    n = len(matriz)
    solucoes = [0] * n

    for i in range(n - 1, -1, -1):
        soma = 0

        for j in range(i + 1, n):
            soma += matriz[i][j] * solucoes[j]

        solucoes[i] = (matriz[i][-1] - soma) / matriz[i][i]

    return solucoes


def resolver_sistema(matriz):
    triangularizar(matriz)
    return retrosubstituicao(matriz)


