# Faça um programa que receba 4 alturas
# usando um laço de repetição e realize a soma dessas alturas.

soma = 0
for i in range(4):
    altura = float(input("Entre com a altura: "))
    soma += altura

print("A soma das alturas é:", soma)