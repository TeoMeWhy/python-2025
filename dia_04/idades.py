# %%
idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)


print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)

