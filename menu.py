import divisorias
import recebeProdutos
import listaFinal
import apagarProdutoDaLista


def showMenu():
    print(">>>> MENU <<<< ")
    print("""
    [1] - Adicionar novos ítens
    [2] - Mostrar a lista
    [3] - Excluir algum ítem  da lista
    [4] - Aterar algum ítem  da lista
    [0] - Finalizar lista de compras""")
    print()
    opc = int(input(">>>>Sua opção: "))
    divisorias.linhaDivisoria()
    match opc:
        case 1:
            recebeProdutos.pegarProduto()
            divisorias.linhaDivisoria()

            showMenu()
        case 2:
            listaFinal.mostrarLista()
            divisorias.linhaDivisoria()
            showMenu()
        case 3:
            print("ESCOLHA O PRODUTO DESEJA REMOVER DA LISTA: ")
            listaFinal.mostrarLista()
            opc = int(input(">>> SUA OPCAO: "))
            recebeProdutos.listaItens.pop(opc-1)
            recebeProdutos.listaValor.pop(opc-1)
            apagarProdutoDaLista.apagarItem("listaItens.txt", opc)
            apagarProdutoDaLista.apagarValor("listaValores.txt", opc)
            showMenu()
        case 0:
            print("Finalizando lista...")
            print("Obrigado e volte sempre")
            divisorias.linhaDivisoria()
            listaFinal.mostrarLista()
        case _:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE:")
            divisorias.linhaDivisoria()
            showMenu()