'''Desenvolva um programa em Python que utilize WHILE para permitir
 o cadatro de um número indeterminado de funcionários. O programa deve 
 encerrar o cadatro quando o usuário digitar 0 e,ao final, exibir a 
 lista completa dos funcionários registrados'''

funcionario= []


while True:
  nome = input("digie o nome do funcionário ( ou 0 para encerrar):")

  if nome == "0":
    break #parada 
  funcionario.append(nome)

print("\nLista de funcionários cadastrados: ")

for funcionario in funcionario :  #enumerate: itera sobre a sequência 
#iterar = repetirr
#enumerate(objeto a ser percorrido , valor inicial do índice)
    print(f"funcionario: {funcionario}")