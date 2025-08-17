'''Crie uma classe Elevador com atributos para andar atual, total de andares 
e capacidade. Implemente métodos para subir e descer andares.
'''

class Elevador:
    def __init__(self, capacidade, total_andares):
        self.andar_atual = 0        # Inicialmente no térreo (andar 0)
        self.capacidade = capacidade
        self.total_andares = total_andares

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"Elevador subiu para o andar {self.andar_atual}.")
        else:
            print("Você já está no último andar.")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"Elevador desceu para o andar {self.andar_atual}.")
        else:
            print("Você já está no térreo.")

# Exemplo de uso
elevador = Elevador(capacidade=8, total_andares=10)
elevador.subir()  # Elevador subiu para o andar 1.
elevador.subir()  # Elevador subiu para o andar 2.
elevador.descer() # Elevador desceu para o andar 1.