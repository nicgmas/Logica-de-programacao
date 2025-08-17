'''Crie uma classe Jogador com atributos para nome e pontos e métodos
para adicionar pontos e zerar a pontuação.
'''

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def adicionar_pontos(self, quantidade):
        if quantidade > 0:
            self.pontos += quantidade
            print(f"{quantidade} pontos adicionados para {self.nome}. Total de pontos: {self.pontos}")
        else:
            print("A quantidade de pontos a adicionar deve ser maior que zero.")

    def zerar_pontos(self):
        self.pontos = 0
        print(f"Pontuação de {self.nome} foi zerada.")

    def __str__(self):
        return f"Jogador: {self.nome}, Pontos: {self.pontos}"


# Exemplo de uso:
jogador = Jogador("Lucas")
print(jogador)            # Jogador: Lucas, Pontos: 0
jogador.adicionar_pontos(10)
jogador.adicionar_pontos(5)
print(jogador)            # Jogador: Lucas, Pontos: 15
jogador.zerar_pontos()
print(jogador)            # Jogador: Lucas, Pontos: 0
Detalhes:
O método adicionar_pontosadiciona pontos (somente se quantidade para positiva).

O método zerar_pontosredefine a pontuação para zero.

O método __str__facilita a exibição das informações do jogador.