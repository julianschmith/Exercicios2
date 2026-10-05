contador = 1
pares = 0
impares = 0
soma_pares = 0
soma_impares = 0

while contador < 11:
    num = int(input(f"Digite o {contador}° número: "))
    if num % 2 == 0:
        pares = pares + 1
        soma_pares = soma_pares + num
    elif num % 2 != 0:
        impares = impares + 1 
        soma_impares = soma_impares + num
    contador = contador + 1

print(f"Tem {pares} numeros pares e {impares} numeros impares")
print(f"\nA soma dos impares é {soma_impares} e a soma dos pares é {soma_pares}")