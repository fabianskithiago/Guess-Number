import random

print("Seja bem vindo ao Guess Number do Thiago!\n")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit(): #FUNÇÃO QUE VERIFICA SE choice_number É UM NÚMERO
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é um numérico. Por favor execute novamente e informe um número!")
    quit()

random_number = random.randint(0,choice_number) #GERA UM NUMERO RANDOMICO ENTRE "0" E O NUMERO QUE O USUARIO DIGITOU

n_choices = 0

while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit(): #FUNÇÃO QUE VERIFICA SE choice_number É UM NÚMERO
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é um numérico. Por favor execute novamente e informe um número!")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou!")
        break

    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso...")

    else:
        print("Chutou baixo, o número randomico é maior que isso...")

print("Numero de tentativas: " + str(n_choices))