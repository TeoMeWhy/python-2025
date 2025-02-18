# %%

txt = "Meu novo arquivo de texto\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)

