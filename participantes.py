from typing import List

def cadastrar_participante(nome: str, participantes: List[str]) -> List[str]:
    """Cadastra um novo participante na lista do grupo."""
    nome_limpo = nome.strip().title()
    if nome_limpo and nome_limpo not in participantes:
        participantes.append(nome_limpo)
    return participantes


def listar_participantes(participantes: List[str]) -> List[str]:
    """Retorna a lista atual de participantes."""
    return participantes.copy()


def verificar_participante(nome: str, participantes: List[str]) -> bool:
    """Verifica se um participante ja esta na lista."""
    return nome.strip().title() in participantes

