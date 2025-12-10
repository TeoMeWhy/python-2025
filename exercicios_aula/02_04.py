# Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Insira seu nome completo: ")
nome = nome.lower()


if 'calvo' in nome:
    print("Essa pessoa é Calvo!")
else:
    print("Essa pessoa não é Calvo!")