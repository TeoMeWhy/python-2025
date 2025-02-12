# Faça um programa que receba um número.
# Verifique se o número informado é par ou ímpar.
# Exiba o resultado da seguinte maneira:

numero = int(input("Entre com um número: "))
# numero = int(numero)

if (numero % 2) == 0:
    print("O número", numero, "é par!")
else:
    print("O número", numero, "é impar!")