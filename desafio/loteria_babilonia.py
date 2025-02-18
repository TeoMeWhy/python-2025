# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número: "))
        
        except ValueError as err:
            print("Valor inválido!")
            continue
                
        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! O valor deve ser entre 1 e 15")


def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print("Parabéns! Você se tornou um milionário de porra nenhuma.")
        return True

    elif usuario > sorteio:
        print("Número muito alto. Tente um número menor!")
        return False

    else:
        print("Número muito baixo. Tente um número maior!")
        return False


numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!!")
