import recebeProdutos

 
def mostrarLista():
#mostrar produtos
    if len(recebeProdutos.listaItens) > 1:
        print( f"---- FIM DA LISTA COM {len(recebeProdutos.listaItens)} ÍTENS---- ")
    else:
         print(f"---- FIM DA LISTA COM {len(recebeProdutos.listaItens)} ÍTEM---- ")
    with open("listaItens.txt", "r") as arquivo:
        mostrarItens = arquivo.read()
        print(mostrarItens)
#mostrar valores
    with open("listaValores.txt", "r") as arquivo:
        mostrarItens = arquivo.read()
        print(mostrarItens)


def mostrarTotal():
    soma = 0
    for i in range(len(recebeProdutos.listaItens)):
        prod = recebeProdutos.listaValor[i]
        soma += prod

    print(f"VALOR TOTAL: R${soma}" )
