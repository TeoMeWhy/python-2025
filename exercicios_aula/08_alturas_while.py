# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0           # valor final
qtde_entradas = 4  # o contador de entradas

while qtde_entradas > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    qtde_entradas -= 1

print("Soma das alturas:", soma)
