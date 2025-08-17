'''Faça uma classe Produto com atributos nome, preço e quantidade em estoque,
e um método para descontar um valor do estoque.'''

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def descontar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida para descontar.")
            return False
        if quantidade > self.quantidade_estoque:
            print(f"Estoque insuficiente para descontar {quantidade} unidades.")
            return False
        self.quantidade_estoque -= quantidade
        print(f"{quantidade} unidades descontadas do estoque de {self.nome}.")
        return True

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}, Estoque: {self.quantidade_estoque}"

# Exemplo de uso
produto = Produto("Caneta", 1.50, 100)
print(produto)                # Produto: Caneta, Preço: R$ 1.50, Estoque: 100

produto.descontar_estoque(10) # 10 unidades descontadas do estoque de Caneta.
print(produto)                # Produto: Caneta, Preço: R$ 1.50, Estoque: 90

produto.descontar_estoque(200) # Estoque insuficiente para descontar 200 unidades.