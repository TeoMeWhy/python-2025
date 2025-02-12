# Faça um programa que receba um número em segundos,
# converta esse número para horas, minuto e segundos.
# Exemplos:
# Entrada: 556
# Saída: 0:9:16
# Entrada: 140153
# Saída: 38:55:53

segundos = input("Entre com os segundos: ")
segundos = int(segundos)

horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)

minutos = segundos // 60
segundos = segundos % 60

print(horas, minutos, segundos, sep=":")