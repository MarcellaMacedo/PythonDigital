print('-' * 38)
print('{:^38}'.format('BANCO 24H'))
print('='* 38)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break
print('='* 38)
print('Obrigada por usar os nossos terminais! \nTenha um bom dia!!!')

