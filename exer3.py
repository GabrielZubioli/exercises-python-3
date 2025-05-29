def eh_numero_armstrong(numero):
    digitos = str(numero)
    n = len(digitos)

    soma = sum(int(digito) ** n for digito in digitos)

    return soma == numero


try:
    numero = int(input("Digite um número para verificar se é um número de Armstrong: "))

    if eh_numero_armstrong(numero):
        print(f"{numero} é um número de Armstrong!")
    else:
        print(f"{numero} NÃO é um número de Armstrong.")

except ValueError:
    print("Erro: Digite um número inteiro válido.")
