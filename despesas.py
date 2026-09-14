from typing import List, Dict


def cadastrar_despesa(
    pagou: str,
    descricao: str,
    valor: float,
    categoria: str,
    despesas: List[Dict],
    participantes: List[str]
) -> List[Dict]:
    """Cadastra uma nova despesa na lista do grupo."""

    pagou_limpo = pagou.strip().title()

    if pagou_limpo in participantes:
        nova_despesa = {
            "pagou": pagou_limpo,
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }

        despesas.append(nova_despesa)

    return despesas


def listar_despesas(despesas: List[Dict]) -> List[Dict]:
    """Retorna uma cópia da lista de despesas."""

    return despesas.copy()


def obter_despesas_por_pessoa(
    despesas: List[Dict],
    pessoa: str
) -> List[Dict]:
    """Retorna apenas as despesas pagas por uma pessoa específica."""

    pessoa_limpa = pessoa.strip().title()

    return [
        despesa for despesa in despesas
        if despesa["pagou"] == pessoa_limpa
    ]

