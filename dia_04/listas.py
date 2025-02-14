# %%

# Uma maneira de definir listas
idades = [28, 42,43, 35,39, 28,38]
print(idades)

# %%
teo = ["Téo", "Calvo", 32, True, "Casado", 2342.98]
print(teo)

# %%
type(teo)

# %%

# idade
print(teo[2])

# renda
print(teo[5])

print(teo[0])

# %%

idades = [28, 42,43, 35,39, 28,38, 42, 34]

soma = sum(idades)
print("soma idades:", soma)

print("qtde idades:", len(idades))

print("media idades:", soma/len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

teo = ["Téo Calvo",
       32,
       True,
       "Casado",
       ["estagiario", "ds jr.", "ds pl", "ds sr.", "head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria", "Claudia"]]

print("Tamanho de téo:", len(teo))

print(teo[6][0])

exs = teo[6]
primeira_ex = exs[0]
print(primeira_ex)

# %%

tamanho = len(teo)
pos = tamanho - 1

exs = teo[pos]
teo[pos][len(exs) - 1]

# %%

teo[-1][-1]

# %%

# primeiros 4 elementos
teo[0:4]

# %%

teo[4][3:5]

# %%
print(teo[4][3:])
print(teo[4][-2:])

# %%
# primeiros 4 elementos
teo[:4]

# %%
# teo[ start : stop ]

# %%

salarios = teo[5]
salarios[::2]

# teo[ start : stop : step ]