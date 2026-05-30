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
    linhas = len(matriz)
    colunas = len(matriz[0]) - 1

    trocas = 0
    linha_pivo = 0

    for coluna in range(colunas):

        melhor_linha = linha_pivo

        while (
            melhor_linha < linhas and
            abs(matriz[melhor_linha][coluna]) < 0.0001
        ):
            melhor_linha += 1

        if melhor_linha == linhas:
            continue

        if melhor_linha != linha_pivo:
            trocar_linhas(
                matriz,
                linha_pivo,
                melhor_linha
            )
            trocas += 1

        pivo = matriz[linha_pivo][coluna]

        for linha in range(linha_pivo + 1, linhas):

            fator = (
                -matriz[linha][coluna] / pivo
            )

            somar_linhas(
                matriz,
                linha_pivo,
                linha,
                fator
            )

        linha_pivo += 1

        if linha_pivo == linhas:
            break

    return matriz, trocas

def determinante_matriz_triangular(matriz, trocas=0):
    determinante = 1

    for i in range(len(matriz)):
        determinante *= matriz[i][i]

    if trocas % 2 != 0:
        determinante *= -1

    return determinante

def retrosubstituicao(matriz):
    linhas = len(matriz)
    variaveis = len(matriz[0]) - 1

    solucoes = [0] * variaveis

    for i in range(linhas - 1, -1, -1):

        coluna_pivo = -1

        for j in range(variaveis):
            if abs(matriz[i][j]) > 0.0001:
                coluna_pivo = j
                break

        if coluna_pivo == -1:
            continue

        soma = 0

        for j in range(
            coluna_pivo + 1,
            variaveis
        ):
            soma += (
                matriz[i][j] * solucoes[j]
            )

        solucoes[coluna_pivo] = (
            matriz[i][-1] - soma
        ) / matriz[i][coluna_pivo]

    return solucoes

# arquivo: funcoes.py

def classificar_sistema(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    quantidade_variaveis = colunas - 1

    rank_coeficientes = 0
    rank_aumentada = 0

    for linha in matriz:

        coeficientes = linha[:-1]

        termo = linha[-1]

        linha_coef_zero = all(
            abs(valor) < 0.0001
            for valor in coeficientes
        )

        linha_total_zero = linha_coef_zero and (
            abs(termo) < 0.0001
        )

        if not linha_coef_zero:
            rank_coeficientes += 1

        if not linha_total_zero:
            rank_aumentada += 1

    if rank_coeficientes < rank_aumentada:
        return "SI"

    if rank_coeficientes < quantidade_variaveis:
        return "SPI"

    return "SPD"

def resolver_sistema(matriz):

    matriz_triangular, trocas = triangularizar(
        matriz
    )

    print("Matriz triangular:")
    imprimir_matriz(matriz_triangular)

    classificacao = classificar_sistema(
        matriz_triangular
    )

    if classificacao != "SPD":
        return None, classificacao

    solucoes = retrosubstituicao(
        matriz_triangular
    )

    return solucoes, classificacao


