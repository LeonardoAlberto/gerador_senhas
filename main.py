import random
import string

letras_minusculas = list(string.ascii_lowercase)
letras_maiusculas = list(string.ascii_uppercase)
numeros = list(string.digits)
simbolos = list(string.punctuation)

while True:
    total_caracteres = input(
        'Digite o nivel da senha desejada:\n  Senha fraca: 1\n  Senha medio: 2\n '
        ' Senha forte: 3\n  Senha muito forte: 4\n  Senha impossivel:  5\n\nSua resposta:  ')


    def gerar(number):
        text = ''
        for i in range(number):
            text += letras_minusculas[random.randint(0, 25)]
            text += letras_maiusculas[random.randint(0, 25)]
            text += numeros[random.randint(0, 9)]
            text += simbolos[random.randint(0, 31)]
        print(text)


    if total_caracteres.isnumeric():
        if 1 <= int(total_caracteres) <= 5:
            if int(total_caracteres) == 1:
                gerar(1)
            elif int(total_caracteres) == 2:
                gerar(2)
            elif int(total_caracteres) == 3:
                gerar(3)
            elif int(total_caracteres) == 4:
                gerar(4)
            elif int(total_caracteres) == 5:
                gerar(11)
        else:
            print('Digite de 1 a 5.')
    else:
        print('Digite numeros.')

    opcao = input('\n\nDeseja criar outra? S/N')
    if not opcao.lower() == 's' and not opcao.lower() == 'sim':
        break
