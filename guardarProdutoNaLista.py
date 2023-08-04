def guardarItens (listaItens, itensDaLista):
    with open("listaItens.txt", "a") as arquivo:
        for item in listaItens:
            arquivo.write(str(item + '\n'))



def guardarValores (listaValores, valoresDaLista):
    with open("listaValores.txt", "a") as arquivo:
        for valor in listaValores:
            arquivo.write(str(valor) + "\n")