'''Crie uma função que receba uma lista de números e retorne uma nova lista 
com os números ordenados em ordem crescente.'''

def ordenar_lista(valores):
    return sorted(valores)

lista = [5,3,8,1,9,2]
lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)