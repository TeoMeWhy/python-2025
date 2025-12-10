# Faça um programa que verifique se o item que
#  a pessoa escolheu para comprar na loja está na lista:
# laranja, cerveja, miojo, carvão, picanha.

items = "laranja cerveja miojo carvão picanha"
escolha = input("Escolha um item: ").lower()

if escolha in items:
    print("Seu item escolhido existe!")
else:
    print("Escolha um item válido!")