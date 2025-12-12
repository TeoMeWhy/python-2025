# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Entre com uma palavra: ").lower()

# Usando método das strings
count = palavra.count("a")

print(f"A palavra '{palavra}' tem {count} 'a'.")