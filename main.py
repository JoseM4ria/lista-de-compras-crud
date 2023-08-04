import recebeProdutos
import listaFinal
import divisorias
import menu


print("---- LISTA DE COMPRAS ----")
recebeProdutos.pegarProduto()
listaFinal.mostrarLista()
divisorias.linhaDivisoria()
menu.showMenu()
listaFinal.mostrarTotal()

print(f"LISTAS: {recebeProdutos.listaItens} / {recebeProdutos.listaValor}")
