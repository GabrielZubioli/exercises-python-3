class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

pessoas = []
while True:
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    email = str(input("Digite o email: "))

    pessoa = Pessoa(nome, idade, email)

    pessoas.append(pessoa)

    opcao = str(input("Deseja criar mais uma pessoa? (sim ou nao): "))

    if opcao == "nao":
        break
    
for pessoa in pessoas:
    print(f"{pessoa.nome}, {pessoa.idade}, {pessoa.email}\n")
