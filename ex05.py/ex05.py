
'''Ler 10 números e imprimir a soma, o maior e o menor'''
numeros = []
        
def ler_numeros():
        soma = 0
        maior = None
        menor = None #None: nenhum valor/valor indefinido


        for i in range(10):
            nu = float(input(f"Digite o {i+1}º número:"))
            #range: gera uma sequência de números inteiros no intervalo

        soma += num

        if maior is None or num > maior:
            maior = numeros

        if menor is None or num < menor :
            menor = num  

            
        print("Soma dos números: {soma}")
        print("Maior número: {maior}")
        print("Menor número: {menor}")

ler_numeros()

