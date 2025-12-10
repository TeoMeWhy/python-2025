# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("Entre com seu nome completo: ")
nome_split = nome.lower().split(" ")

if "calvo" in nome_split:  # "teo calvo" -> ["teo", "calvo"]
    print("Essa pessoa é Calvo")

if "silva" in nome_split: # silvana calvo -> ["silvana", "calvo"]
    print("Essa pessoa é Silva")

if "silva" not in nome_split and "calvo" not in nome_split:
    print("Essa pessoa não é Silva, nem Calvo")