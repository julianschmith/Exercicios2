contador = 1
soma = 0

while contador < 11:
    num = int(input(f"Digite o {contador}° número: "))
    soma = soma + num
    contador = contador + 1

print(f"A soma de todos os numeros é {soma}")