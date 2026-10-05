soma_pares = 0
media_pares = 0

for i in range(1, 6):
    num = int(input(f"Digite o {i}° numero: "))
    if num % 2 == 0:
        soma_pares = soma_pares + num

if soma_pares > 0:
    media_pares = soma_pares / 5

print(f"A média dos números pares é: {media_pares}")