# Faça um programa que receba uma quantidade indefinida de valores
# correspondentes a “saldo em conta”,
# mas quando o usuário apertar “enter” sem digitar valor algum,
# o programa para de receber valores, e exibe a soma de todos os
# valores digitados anteriormente.


soma = 0

while True:
    entrada = input("Entre com um valor: ")
    
    if entrada == "":
        break

    soma += float(entrada)

print(f"A soma total dos valores é: R${soma}")