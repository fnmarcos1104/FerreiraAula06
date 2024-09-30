import os

os.system('cls')

minha_lista = []

minha_lista2 = [5, 3, 9, 4, 11]

texto = 'python'

# print(minha_lista2[1])    #Verificar qual é o valor através da posição (Usar -1 para achar último elemento da lista).
# print(len(minha_lista2))    #Informa o tamanho da lista.
# print(minha_lista2[1:4])    #Informa lista fatiada 

# minha_lista2.append(5)    #Inserir valor no fim da lista.
# minha_lista2.insert(2, 100)    #Inserir valor em posição específica.

# print(minha_lista2.index(11))    #Aponta a posição do valor inserido.
# i = minha_lista2.index(11)
# print(i)

# minha_lista2.remove(4)    #Remove valor através do valor escolhido.
# print(minha_lista2.pop(3))    #Remove valor através da posição do valor
# print(minha_lista2)
minha_lista2.clear()   #Limpar lista


lista_ord = ['a', 'c', 'b']
# lista_ord.reverse()    #Mostra lista ao contrário
# print(lista_ord)

# lista_ord.sort()    #Organiza a lista
lista_ord.sort(reverse=True)    #Organiza a lista de trás para frente.
# lista_ord.sort(reverse=False)  #Organiza a lista de frente para trás.

print(lista_ord)