nome = input('Digite seu nome: ')

while True:
    altura = input('Digite sua altura: ')
    if '.' in altura:
        break
    print('Por favor, insira a altura usando o separador decimal (.)')

altura = float(altura)
peso = float(input('Digite seu peso: '))

IMC = peso / (altura ** 2)

if (IMC < 16):
    print(f'{nome}, seu status é:\nMagreza Grave !!!')

elif (IMC >= 16) and (IMC < 17):
    print(f'{nome}, seu status é:\nMagreza moderada ')

elif (IMC >= 17) and (IMC < 18.5):
    print(f'{nome}, seu status é:\nMagreza leve ')

elif (IMC >= 18.5) and (IMC < 25):
    print(f'{nome}, seu status é:\nSaudável !!!')

elif (IMC >= 25) and (IMC < 30):
    print(f'{nome}, seu status é:\nSobrepeso')

elif (IMC >= 30) and (IMC < 35):
    print(f'{nome}, seu status é:\nObesidade Grau I ')

elif (IMC >= 35) and (IMC < 40):
    print(f'{nome}, seu status é:\nObesidade Grau II (severa)')

elif (IMC > 40):
    print(f'{nome}, seu status é:\nObesidade Grau III (mórbida) ')

else:
    print('Você digitou algo errado !!!')
