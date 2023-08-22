import apagarProdutoDaLista


def editarProduto(alterar, novoProduto):]
    with open("listaItens.txt", "w") as arquivoWrite:
        lines = arquivoWrite.readlines()
        for line in lines:
            arquivoWrite.write(line)

    ##with open("listaItens.txt", "r") as arquivoRead:
      #  lines = arquivoRead.readlines()
       # ptr = 1

        #with open("listaItens.txt", "w") as arquivoWrite:
         #   for line in lines:
          #      if ptr != alterar:
           #         arquivoWrite.write(line)
            #    ptr += 1
    #with open("listaItens.txt", "a" ) as arquivoNew:
     #   arquivoNew.write(novoProduto)


def editarValor(alterar, novoValor):
    with open("listaValores.txt", "w") as arquivoWrite:
        lines = arquivoWrite.readlines()
        for line in lines:
            arquivoWrite.write(str(lines))

    # with open("listaValores.txt", "r") as arquivoRead:
      #  lines = arquivoRead.readlines()
       # ptr = 1
        #with open("listaValores.txt", "w") as arquivoWrite:
         #   for line in lines:
          #      if ptr != alterar:
           #         arquivoWrite.write(line)
            #    ptr += 1
   # with open("listaValores.txt", "a" ) as arquivoNew:
    #    arquivoNew.write(novoValor)