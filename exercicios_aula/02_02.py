# 02 Altere o programa anterior para considerar a quantidade de garrafas de água

tipo = input("Escolha um tipo de água: (1) Água Mineral Natural / (2) Água Mineral com Gás ")
qtde = int(input("Qual a quantidade de garrafas? "))

if tipo == "1":
    valor = 1.5 * qtde
    print("Total: R$", valor)

elif tipo == "2":
    valor = 2.5 * qtde
    print("Total: R$", valor)

else:
    print("Entre com dados válidos!")
