# Escreva um programa que receba o nome e a idade de uma pessoa.
# Depois exiba a mensagem: “Olá fulano, bom saber que você tem x anos. Boas vindas!”

nome = input("Entre com o seu nome: ")
idade = input("Quantos anos você tem? ")

msg = f"""
Olá, {nome}!

Bom saber que você tem {idade} anos.

Boas vindas!
"""

print(msg)