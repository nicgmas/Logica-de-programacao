'''Crie uma classe Banco com um método para adicionar clientes
(objetos da classe Cliente) e outro para listar todos os clientes.
'''

class Clientes:
    def __init__ (self,nome,senha):
        self.nome
        self.senha
        
    def __str_(self):
        return f"Cliente: {self.nome}, senha: {self.senha}"
    
    
class Banco:
    def __init__(self):
        self.clientes = []
        
    def adicionar_clientes(self, cliente):
        self.cliente.append(cliente)  
        print(f"Cliente {cliente.nome} adicionado com sucesso.")
        
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastro.")
        else: 
            print("Lista de clientes:")
        for cliente in self.clientes:
            print("cliente")
            
            