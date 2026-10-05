nome = str(input("Digite o seu nome: "))
ano_nascimento = int(input("Agora, digite o seu ano de nascimento: "))
ano_atual = int(input("Escreva o ano atual: "))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print("Você já é de maior e pode fazer a carteira de motorista.")
elif idade < 18 and idade >= 16:
    print("Você já pode votar")
else:
    print("Voce não pode fazer nada")