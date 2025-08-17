'''Implemente uma função que recebe uma lista de números e retorna True 
se todos eles forem positivos.'''

def todos_positivos_usuario():
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista_str = entrada.split()
    lista_numeros = []
    
    for item in lista_str:
        try:
            numero =float(item)
            lista_numeros.append(numero)
        except ValuerError:
            print(f"'{item} não é um número válido.")
            return False
            
    for numero in lista_numeros:
        if numero <= 0:
            return False
    return True

resultado = todos_positivos_usuario()
print(resultado)
            