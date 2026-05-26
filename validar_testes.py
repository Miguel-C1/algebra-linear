import numpy as np

from copy import deepcopy

from funcoes import (
    triangularizar,
    determinante_matriz_triangular,
    resolver_sistema
)

from test import *


TOLERANCIA = 0.0001


# =====================================
# VALIDAÇÃO DE DETERMINANTE
# =====================================

def validar_determinante(nome, matriz):
    try:
        matriz_copia = deepcopy(matriz)

        matriz_triangular, trocas = triangularizar(
            matriz_copia
        )

        meu_resultado = determinante_matriz_triangular(
            matriz_triangular,
            trocas
        )

        numpy_resultado = np.linalg.det(
            np.array(matriz, dtype=float)
        )

        sucesso = abs(
            meu_resultado - numpy_resultado
        ) < TOLERANCIA

        print(f"[{'OK' if sucesso else 'ERRO'}] {nome}")

        print(
            f"Meu determinante : "
            f"{meu_resultado}"
        )

        print(
            f"Numpy             : "
            f"{numpy_resultado}"
        )

        print()

    except Exception as erro:
        print(f"[ERRO] {nome}")
        print(f"Exceção: {erro}")
        print()


# =====================================
# VALIDAÇÃO DE SISTEMAS LINEARES
# =====================================

def validar_sistema(nome, matriz):
    try:
        matriz_copia = deepcopy(matriz)

        meu_resultado, classificacao = resolver_sistema(
            matriz_copia
        )

        matriz_np = np.array(
            matriz,
            dtype=float
        )

        A = matriz_np[:, :-1]
        B = matriz_np[:, -1]

        numpy_resultado = np.linalg.solve(
            A,
            B
        )

        sucesso = True

        for i in range(len(meu_resultado)):
            if abs(
                meu_resultado[i] -
                numpy_resultado[i]
            ) > TOLERANCIA:

                sucesso = False
                break

        print(f"[{'OK' if sucesso else 'ERRO'}] {nome}")

        print(
            f"Meu resultado : "
            f"{meu_resultado}"
        )
        print(
            f"Classificação : "
            f"{classificacao}"
        )
        print(
            f"Numpy          : "
            f"{numpy_resultado}"
        )

        print()

    except np.linalg.LinAlgError as erro:
        print(f"[ERRO NUMPY] {nome}")
        print(f"Numpy informou: {erro}")
        print()

    except Exception as erro:
        print(f"[ERRO] {nome}")
        print(f"Exceção: {erro}")
        print()


# =====================================
# TESTES DE DETERMINANTES
# =====================================

validar_determinante(
    "matriz_2x2_simples",
    matriz_2x2_simples
)

validar_determinante(
    "matriz_2x2_det_negativa",
    matriz_2x2_det_negativa
)

validar_determinante(
    "matriz_2x2_troca_linha",
    matriz_2x2_troca_linha
)

validar_determinante(
    "matriz_2x2_singular",
    matriz_2x2_singular
)

validar_determinante(
    "matriz_2x2_negativos",
    matriz_2x2_negativos
)

validar_determinante(
    "matriz_2x2_decimais",
    matriz_2x2_decimais
)

validar_determinante(
    "matriz_3x3_simples",
    matriz_3x3_simples
)

validar_determinante(
    "matriz_3x3_troca_linha",
    matriz_3x3_troca_linha
)

validar_determinante(
    "matriz_3x3_singular",
    matriz_3x3_singular
)

validar_determinante(
    "matriz_3x3_triangular",
    matriz_3x3_triangular
)

validar_determinante(
    "matriz_3x3_negativos",
    matriz_3x3_negativos
)

validar_determinante(
    "matriz_3x3_decimais",
    matriz_3x3_decimais
)

validar_determinante(
    "matriz_3x3_pivo_pequeno",
    matriz_3x3_pivo_pequeno
)

validar_determinante(
    "matriz_4x4_normal",
    matriz_4x4_normal
)

validar_determinante(
    "matriz_4x4_singular",
    matriz_4x4_singular
)

validar_determinante(
    "matriz_4x4_trocas",
    matriz_4x4_trocas
)

validar_determinante(
    "matriz_4x4_triangular_inferior",
    matriz_4x4_triangular_inferior
)

validar_determinante(
    "matriz_4x4_decimais",
    matriz_4x4_decimais
)

validar_determinante(
    "matriz_5x5_normal",
    matriz_5x5_normal
)

validar_determinante(
    "matriz_5x5_singular",
    matriz_5x5_singular
)

validar_determinante(
    "matriz_5x5_zeros",
    matriz_5x5_zeros
)

validar_determinante(
    "matriz_5x5_quase_singular",
    matriz_5x5_quase_singular
)


# =====================================
# TESTES DE SISTEMAS LINEARES
# =====================================

validar_sistema(
    "sistema_3x3",
    sistema_3x3
)

validar_sistema(
    "sistema_pivo_zero",
    sistema_pivo_zero
)
