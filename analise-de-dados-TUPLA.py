num = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
    print('O valor 9 não foi digitado em nenhuma posição')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(9)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')


