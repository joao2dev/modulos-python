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

participantes = []

# Testa cadastro
participantes = cadastrar_participante("João", participantes)
print(participantes)  # Deve imprimir: ["João"]

participantes = cadastrar_participante("Maria", participantes)
print(participantes)  # Deve imprimir: ["João", "Maria"]

# Testa se aceita duplicata (não deve)
participantes = cadastrar_participante("João", participantes)
print(participantes)  # Deve imprimir: ["João", "Maria"] (sem adicionar novamente)

# Testa verificação
existe = verificar_participante("João", participantes)
print(existe)  # Deve imprimir: True

existe = verificar_participante("Pedro", participantes)
print(existe)  # Deve imprimir: False

# Testa listagem
lista = listar_participantes(participantes)
print(lista)  # Deve imprimir: ["João", "Maria"]