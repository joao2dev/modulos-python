from typing import List
from calculos import calcular_total_gastos,calcular_gastos_individuais,calcular_saldo_individual,calcular_valor_medio_por_pessoa


participantes_teste = ["João", "Maria","Pedro"]

def imprimir_total_de_gastos(despesas: List[dict]) -> None:
    """Imprime o valor total de gastos da viagem"""
    total = calcular_total_gastos(despesas)
    print(f"Total: R${total:.2f}")

def imprimir_gastos_individual(despesas: List[dict]) -> None:
    """Imprime quanto cada particiapante pagou"""
    gastos = calcular_gastos_individuais(despesas)
    for pessoa,valor in gastos.items():
        print(f"{pessoa}: R${valor:.2f}")

def imprimir_valor_por_pessoa(despesas: List[dict], participantes: List[str]) -> None:
    """Imprime quanto cada participante vai ter que pagar"""
    media = calcular_valor_medio_por_pessoa(despesas,participantes)
    print(f"valor por pessoa: R${media:.2f}")


def imprimir_saldo_individual(despesas: List[dict], participantes:List[str] ) -> None:
    """Imprime o saldo de cada participonte"""
    saldo = calcular_saldo_individual(despesas,participantes)
    for pessoa,valor in saldo.items():
        if valor > 0:
            print(f"{pessoa}: +R${valor:.2f}")
        elif valor < 0:
                print(f"{pessoa}: -R${abs(valor):.2f}")
        else:
            print(f"{pessoa}: R${valor:.2f}")

def imprimir_relatorio(despesas: List[dict], participantes: List[str]) -> None:
    """Imprime relatorio completo"""
    imprimir_gastos_individual(despesas)
    print("")
    imprimir_total_de_gastos(despesas)
    imprimir_valor_por_pessoa(despesas, participantes)
    print("")
    imprimir_saldo_individual(despesas, participantes)

despesas_teste = [
    {"pagou": "João", "descricao": "Almoço", "valor": 150.0, "categoria": "Alimentação"},
    {"pagou": "Maria", "descricao": "Gasolina", "valor": 80.0, "categoria": "Transporte"},
    {"pagou": "Pedro", "descricao": "Cinema", "valor": 60.0, "categoria": "Diversão"}
]
relatorio = imprimir_relatorio(despesas_teste,participantes_teste)
