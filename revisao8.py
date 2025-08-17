'''Implemente uma classe Telefone com atributos para marcar número,
mostrar histórico de chamadas e desligar.'''

class Telefone:
    def __init__(self):
        self.historico_chamadas = []
        self.em_chamada = False
        self.numero_em_chamada = None

    def marcar_numero(self, numero):
        if self.em_chamada:
            print(f"Já está em uma chamada com {self.numero_em_chamada}. Desligue antes de ligar para outro número.")
            return
        self.em_chamada = True
        self.numero_em_chamada = numero
        self.historico_chamadas.append(numero)
        print(f"Chamando o número {numero}...")

    def mostrar_historico(self):
        if not self.historico_chamadas:
            print("Nenhuma chamada realizada.")
        else:
            print("Histórico de chamadas:")
            for i, num in enumerate(self.historico_chamadas, 1):
                print(f"{i}: {num}")

    def desligar(self):
        if self.em_chamada:
            print(f"Desligando a chamada com {self.numero_em_chamada}.")
            self.em_chamada = False
            self.numero_em_chamada = None
        else:
            print("Nenhuma chamada ativa para desligar.")


# Exemplo de uso
telefone = Telefone()

telefone.marcar_numero("1234-5678")
telefone.mostrar_historico()
telefone.desligar()
telefone.desligar()
telefone.marcar_numero("8765-4321")
telefone.mostrar_historico()