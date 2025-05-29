jogador1 = int(input("(Jogador 1) Escolha uma das opções [1-Pedra | 2-Papel | 3-Tesoura]\n"))
jogador2 = int(input("(Jogador 2) Escolha uma das opções [1-Pedra | 2-Papel | 3-Tesoura]\n"))

messagem1 = str("Jogador 1 Venceu!")
messagem2 = str("Jogador 2 Venceu!")
messagemEmpate = str("Empate!")

if jogador1 == jogador2 :
    print(messagemEmpate)
elif jogador1 == 1 and jogador2 == 3 or jogador1 == 2 and jogador2 == 1 or jogador1 == 3 and jogador2 == 2:
    print(messagem1)
else:
    print(messagem2)
    