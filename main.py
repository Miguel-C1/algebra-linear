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
#sistema_3x3 = [
#    [2, 1, -1, 8],
#    [-3, -1, 2, -11],
#    [-2, 1, 2, -3]
#]
# No arquivo test.py, existem várias matrizes de teste, incluindo sistemas aumentados. Você pode escolher um deles para validar a função de resolução de sistemas lineares. 
# Por exemplo, você pode usar o sistema_3x3 ou criar um novo sistema de acordo com suas necessidades.

matriz = sistema_3x3

print("Matriz original:")
imprimir_matriz(matriz)

solucao, classificacao = resolver_sistema(matriz)

print(f"Solução do sistema: {solucao}")
print(f"Classificação do sistema: {classificacao}")
