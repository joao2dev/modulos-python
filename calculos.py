from typing import List, Dict
from participantes import listar_participantes

participantes = listar_participantes(["João", "Maria", "Pedro"])

def calcular_total_gastos(despesas: List[dict]) -> float:
    """Calcula o valor total gasto em todas as despesas."""
    total = 0.0
    for despesa in despesas:
        total+= despesa["valor"]
    return total

def calcular_gastos_individuais(despesas: List[dict] ) -> Dict[str, float]:
    """Calcula quanto cada participante pagou no total."""
    gasto_por_pessoas = {}
    for despesa in despesas:
        pessoa = despesa["pagou"]
        valor = despesa["valor"]
        if pessoa not in gasto_por_pessoas:
            gasto_por_pessoas[pessoa] = 0.0

        gasto_por_pessoas[pessoa] += valor

    return gasto_por_pessoas

def calcular_valor_medio_por_pessoa(despesas: List[dict], participantes: List[str]) -> float:
    """Calcula quanto cada pessoa deveria pagar (divisão igual do total)."""
    total = calcular_total_gastos(despesas)
    media = total / len(participantes)
    return media
def calcular_saldo_individual(despesas: List[dict], participantes: List[str]) -> Dict[str, float]:
    """Calcula o saldo de cada participante."""
    gastos = calcular_gastos_individuais(despesas)
    media = calcular_valor_medio_por_pessoa(despesas, participantes)
    saldo_individual = {}
    for pessoa in participantes:
        quanto_pagou = gastos.get(pessoa, 0.0)  # Se não pagou nada, retorna 0
        saldo_individual[pessoa] = quanto_pagou - media

    return saldo_individual





despesas_teste = [
    {"pagou": "João", "descricao": "Almoço", "valor": 150.0, "categoria": "Alimentação"},
    {"pagou": "Maria", "descricao": "Gasolina", "valor": 80.0, "categoria": "Transporte"},
    {"pagou": "João", "descricao": "Cinema", "valor": 60.0, "categoria": "Diversão"}
]

resultado = calcular_saldo_individual(despesas_teste, participantes)
print(resultado)
# Deve imprimir algo como:
# {"João": 113.33, "Maria": -16.67, "Pedro": -96.67}
# Deve imprimir: 96.66666... (290 / 3)