import random
import os
os.system('clear')

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+,-./:;<=>?@[\]_{|}'

print('Bem Vindo ao Gerador de Senhas\n')
print('Digite [1] para senha de segurança baixa\nDigite [2] para senha de segurança média\nDigite [3] para senha de segurança alta\nDigite [4] para senha de segurança muito alta\n')

while True:
    try:
        kind = int(input('Qual nível de segurança desejado para sua senha? '))
        if not 1 <= kind <= 4:
            raise ValueError('escolha entre as opções indicadas')
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

os.system('clear')

print('Sua senha pode ser gerada com um mínimo de 6 caracteres e um maximo de 18 caracteres.\n')

while True:
    try:
        length = int(input('Qual a quantidade de caracteres da senha? '))
        if not 6 <= length <= 18:
            raise ValueError('valor fora do limite')
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

os.system('clear')

if kind == 1:
    password = lower
elif kind == 2:
    password = lower + numbers
elif kind == 3:
    password = lower + upper + numbers
else:
    password = lower + upper + numbers + symbols

kind_dict = {1: 'apenas letras minúsculas.', 2: 'apenas letras minúsculas e números.', 3: 'letras minúsculas, maiúsculas e números.', 4: 'letras minúsculas, maiúsculas, números e símbolos.'}

print('A senha gerada aleatoriamente contém {} caracteres e é composta por {}\n'.format(length,kind_dict[kind]))

password = ''.join(random.sample(password, length))

print('Nova senha gerada: {}\n'.format(password))