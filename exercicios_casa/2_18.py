dados = {}

while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, "->", j)