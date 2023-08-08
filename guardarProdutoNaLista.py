def guardarItens (listaItens ):
    with open("listaItens.txt", "w") as arquivo:
        for item in listaItens:
            arquivo.write(str(item + '\n'))



def guardarValores (listaValores ):
    with open("listaValores.txt", "w") as arquivo:
        for valor in listaValores:
            arquivo.write(str(valor) + "\n")