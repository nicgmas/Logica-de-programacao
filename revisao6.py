'''Crie uma classe Funcionario que armazena nome e salário, e um método que
retorna um aumento salarial de 10%.'''

 def aumentar_salario(self):
        aumento = self.salario * 0.10
        self.salario += aumento
        return self.salario

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: R$ {self.salario:.2f}"


# Exemplo de uso
func = Funcionario("Ana", 3000.00)
print(func)             # Funcionário: Ana, Salário: R$ 3000.00
func.aumentar_salario()
print(func)             # Funcionário: Ana, Salário: R$ 3300.00