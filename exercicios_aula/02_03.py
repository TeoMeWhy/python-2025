# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo = input("Entre com o tipo o sorvete: [Casquinha (R$1,00) / Cascão (R$2,50) / Cestinha (R$4,00)] ")
tipo = tipo.lower()

sabor = input("Escolha o seu sabor: [Morango / Creme / Chocolate] ")
sabor = sabor.lower()

cobertura = input("Escolha a cobertura: [Caramelo (R$1,50) / Morango (R$1,50) / Chocolate (R$1,50) / Sem cobertura (R$0,00)]")
cobertura = cobertura.lower()

valor = 0
if tipo == "casquinha":
    valor += 1
elif tipo == "cascão":
    valor += 2.5
elif tipo == "cestinha":
    valor += 4

if cobertura in ["caramelo", "morango", "chocolate"]:
    valor += 1.5

txt = f"Seu sorverte {tipo} de {sabor} com cobertura de {cobertura} custou R${valor:.2f}"
print(txt)