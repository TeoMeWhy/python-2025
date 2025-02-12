# Faça um programa que receba uma quantidade indefinida
# de valores correspondentes a “saldo em conta”,
# mas quando o usuário apertar “enter” sem digitar valor algum,
# o programa para de receber valores, e exibe a soma
# de todos os valores digitados anteriormente.

saldo_total = 0
while True:
    saldo = input("Entre com o saldo: ")

    if saldo == "":
        break

    saldo_total += float(saldo)

print("Saldo total:", saldo_total)
