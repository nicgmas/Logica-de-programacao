'''Faça uma classe Relogio com métodos para mostrar o horário atual 
e ajustar o horário manualmente.'''

from datetime import datetime


class Relogio:
    def __init__(self):
        self.ajuste_manual = None

    def mostrar_horario(self):
        horario = self.ajuste_manual or datetime.now()
        print("Horário atual:", horario.strftime("%H:%M:%S"))

    def ajustar_horario(self, hora, minuto, segundo=0):
        try:
            agora = datetime.now()
            self.ajuste_manual = agora.replace(hour=hora, minute=minuto, second=segundo, microsecond=0)
            print(f"Horário ajustado para {self.ajuste_manual.strftime('%H:%M:%S')}")
        except ValueError:
            print("Horário inválido. Por favor, insira valores válidos para hora, minuto e segundo.")


# Exemplo de uso
rel = Relogio()
rel.mostrar_horario()
rel.ajustar_horario(15, 30, 0)
rel.mostrar_horario()