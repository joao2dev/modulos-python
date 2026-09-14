from participantes import *
from despesas import *
from realatorio import *
def main() -> None:
    cadastro = int(input("Quantos participantes você deseja cadastrar? "))
    participantes = []
    despesas = []
    for i in range(cadastro):
        participante = str(input(f"Informe o nome do {i+1} participante: "))
        cadastrar_participante(participante,participantes)
    if not participantes:
        print("nenhum participante cadastrado")
        return

    print(listar_participantes(participantes))
    for j in range(cadastro):
        pagamento = float(input(f"{participantes[j]} pagou R$"))
        if pagamento > 0.0:
            cadastrar_despesa(participantes[j],"descriçãp",pagamento,"categoria",despesas,participantes)
        else:
            pass
    listar_despesas(despesas)

    imprimir_relatorio(listar_despesas(despesas),
        listar_participantes(participantes))
if __name__ == "__main__":
    main()