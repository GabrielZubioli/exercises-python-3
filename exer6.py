def criarCarro(nome, ano):
    carro = {
        "Nome" : nome,
        "Ano" : ano
    }
    return carro

nome = str(input("Qual o nome do seu carro : "))
ano = int(input("Qual o ano do seu carro : "))

carro = criarCarro(nome, ano)

print(f"Nome : {carro['Nome'] }\nAno : {carro['Ano']}")
