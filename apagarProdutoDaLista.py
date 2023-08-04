import listaFinal
import recebeProdutos

def apagarItem (listaItens, apagarLinha):
    with open("listaItens.txt", "r") as arquivoRead:
        lines = arquivoRead.readlines()
        ptr = 1

        with open("listaItens.txt", "w") as arquivoWrite:
            for line in lines:
                if ptr != apagarLinha:
                    arquivoWrite.write(line)
                ptr += 1


def apagarValor(listaItens, apagarLinha):
    with open("listaValores.txt", "r") as valoresRead:
        lines = valoresRead.readlines()
        ptr = 1

        with open("listaValores.txt", "w") as valoresWrite:
            for line in lines:
                if ptr != apagarLinha:
                    valoresWrite.write(line)
                ptr += 1


    print("LISTA ATUALIZADA: ")
    listaFinal.mostrarLista()
