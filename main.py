from funcoes import (
    determinante_matriz_triangular,
    imprimir_matriz,
    resolver_sistema,
    triangularizar
)
from test import *
# Matriz aumentada do sistema
# Exemplo:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

matriz = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

print("Matriz original:")
imprimir_matriz(matriz)

matriz_triangular, trocas = triangularizar(matriz)

print("Matriz triangular:")
imprimir_matriz(matriz_triangular)

print("Determinante da matriz triangular:", determinante_matriz_triangular(matriz_triangular, trocas))
print("Número de trocas de linhas:", trocas)

solucao, classificacao = resolver_sistema(matriz_triangular)

print("Solução do sistema:")
print(f"Solução do sistema: {solucao}")
print(f"Classificação do sistema: {classificacao}")
