import math

def calcular_pontos_dardos(x, y):
    distancia = math.sqrt(x**2 + y**2)

    if distancia <= 1:
        return 10 
    elif distancia <= 5:
        return 5 
    elif distancia <= 10:
        return 1
    else:
        return 0 

try:
    x = float(input("Digite a coordenada X do dardo: "))
    y = float(input("Digite a coordenada Y do dardo: "))

    pontos = calcular_pontos_dardos(x, y)

    print(f"O dardo caiu na posição ({x}, {y}) e ganhou {pontos} pontos.")

except ValueError:
    print("Erro: Digite apenas números válidos.")
