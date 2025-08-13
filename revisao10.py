'''Escreva um programa que peça uma palavra ao usuário e 
imprima essa palavra invertida.'''

palavra = input("Digite uma palavra: ")
converte = " " .join(reversed(palavra))
print(converte)