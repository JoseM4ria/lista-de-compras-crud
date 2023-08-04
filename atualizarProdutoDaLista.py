alt = ""
def editarProduto():
    alterar = int(input("Qual produto você deseja ALTERAR? "))
    alt = alterar
    novoProduto = input("Novo ítem: ")

    with open("listaItens.txt", "r") as arquivoRead:
        lines = arquivoRead.readlines()
        ptr = 1

        with open("listaItens.txt", "w") as arquivoWrite:
            for line in lines:
                if ptr != alterar:
                    arquivoWrite.write(line)
                ptr += 1
    with open("listaItens.txt", "a" ) as arquivoNew:
        arquivoNew.write(novoProduto)


def editarValor():
    novoValor = input("Valor: R$")

    with open("listaValores.txt", "r") as arquivoRead:
        lines = arquivoRead.readlines()
        ptr = 1

        with open("listaValores.txt", "w") as arquivoWrite:
            for line in lines:
                if ptr != alt:
                    arquivoWrite.write(line)
                ptr += 1

    with open("listaValores.txt", "a" ) as arquivoNew:
        arquivoNew.write(novoValor)