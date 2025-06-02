class Carro: 
    def __init__(self, nome, modelo, ano):
        self.nome = nome
        self.modelo = modelo
        self.ano = ano

nome = str(input("Qual o nome do carro :"))
modelo = str(input("Qual o modelo do carro :"))
ano = int(input("Qual o ano do carro :"))

carro1 = Carro(nome, modelo, ano)

print(f"Nome: {carro1.nome}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

