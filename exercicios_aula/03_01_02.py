# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Entre com uma palavra: ").lower()

count = 0

for letra in palavra:
    count += int(letra == "a")

print(f"A palavra '{palavra}' tem {count} 'a'.")