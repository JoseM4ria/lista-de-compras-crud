import divisorias
import guardarProdutoNaLista
import recebeProdutos
import listaFinal
import apagarProdutoDaLista
import atualizarProdutoDaLista


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
            listaFinal.mostrarLista()
            divisorias.linhaDivisoria()
            showMenu()
        case 2:
            listaFinal.mostrarLista()
            divisorias.linhaDivisoria()
            showMenu()
        case 3:
            print("ESCOLHA O PRODUTO DESEJA REMOVER DA LISTA: ")
            print(f"Escolha entre [1] e [{len(recebeProdutos.listaItens)}]")
            divisorias.linhaDivisoria()
            listaFinal.mostrarLista()
            divisorias.linhaDivisoria()
            opc = int(input(">>> SUA OPCAO: "))
            recebeProdutos.listaItens.pop(opc - 1)
            recebeProdutos.listaValor.pop(opc - 1)
            apagarProdutoDaLista.apagarItem("listaItens.txt", opc)
            apagarProdutoDaLista.apagarValor("listaValores.txt", opc)

            showMenu()
        case 4:
            print("Qual produto você deseja ALTERAR? ")
            print(f"Escolha entre [1] e [{len(recebeProdutos.listaItens)}]")
            divisorias.linhaDivisoria()
            listaFinal.mostrarLista()
            divisorias.linhaDivisoria()
            opc = int(input(">>>>Sua opção: "))
            alterar = opc - 1
            novoProduto = input("Novo ítem: ")
            novoValor = float(input("Valor: R$"))
            recebeProdutos.listaItens[alterar] = novoProduto
            recebeProdutos.listaValor[alterar] = novoValor
            guardarProdutoNaLista.guardarItens(recebeProdutos.listaItens)
            guardarProdutoNaLista.guardarValores(recebeProdutos.listaValor)
            # atualizarProdutoDaLista.editarProduto(alterar, novoProduto)
            # atualizarProdutoDaLista.editarValor(alterar,novoValor)
            listaFinal.mostrarLista()
            showMenu()
        case 0:
            divisorias.linhaDivisoria()
            print("Finalizando lista...")
            print("Obrigado e volte sempre")
            divisorias.linhaDivisoria()
            listaFinal.mostrarLista()
        case _:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE:")
            divisorias.linhaDivisoria()
            showMenu()
