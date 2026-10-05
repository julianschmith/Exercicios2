maior_idade = 0
nome_mais_velho = ""

for i in range(1, 6):
    nome = str(input(f"Digite o {i}° nome: "))
    idade = int(input(f"Digite a idade do {i}° nome: "))

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

print(f"O nome da pessoa mais velha é {nome_mais_velho} e a idade é {maior_idade}")