def criarCarro(nome, ano):
    carro = (nome, ano)
    return carro

nome = str(input("Qual o nome do seu carro :"))
ano = int(input("Qual o ano do seu carro : "))

carro = criarCarro(nome, ano)

print(f"Nome: {carro[0]}\n Ano: {carro[1]}")