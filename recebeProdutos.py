from divisorias import linhaDivisoria
import guardarProdutoNaLista

listaItens = []
listaValor = []


def pegarProduto():
    while True:
        item = input("Produto: ")
        listaItens.append(item)
        valor = float(input("Valor: R$"))
        listaValor.append(valor)
        opc = input("DESEJA CONTINUAR? [S/N]: ").upper()
        linhaDivisoria()

        while opc != "N" and opc != "S":
            print("APENAS VALORES [N] OU [S], TENTE NOVAMENTE:")
            opc = input("DESEJA CONTINUAR? [S/N]: ").upper()
            linhaDivisoria()
        if opc == "S":
            continue
        elif opc == "N":
            guardarProdutoNaLista.guardarItens(listaItens, "listaItens.txt")
            guardarProdutoNaLista.guardarValores(listaValor, "listaValores.txt")
            break
