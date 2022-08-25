pessoas = [] 
masc = 0
fem = 0

print("Seletor De Pessoas")
while True:
    sexo = str(input("Escreva seu sexo [F/M]: ")).lower() ##.lower() para deixar o que for digitado em caixa baixa
    idade = int(input("Escreva sua idade: "))

    print("""
    [1]Preto
    [2]Castanho
    [3]Loiro
    [4]Ruivo
    """)

    cor_cabelo = int(input("Digite a cor do seu cabelo: "))
    choice = str(input("Você quer continuar?S/n ")).lower()
    print("\n")

    usuario = {"sexo": sexo, "cor_cabelo": cor_cabelo, "idade": idade} ##Defininndo as informações do usuário
    pessoas.append(usuario) ##Salvando na lista pessoas
    ##Verificação das condicionais
    if sexo == "m" and idade >= 18 and cor_cabelo == 2:
        masc += 1
    elif sexo == "f" and idade >= 25 and idade <= 30 and cor_cabelo == 3:
        fem += 1

    if choice == "s":
        continue ##Esse comando reinicia o loop
    else:
        break

    
for i in pessoas:
    for n in i:
        print(f"{n}:{i[n]}")
    print("\n")


print(f"O total de homens +18 e com a cor do cabelo castanho é : {masc}")
print(f"O total de mulheres entre 25 e 30 anos com a cor do cabelo loiro é: {fem}")
    





