listagem = ('Lápis',1.75, 'Borracha', 2, 'Apontador', 3, 'Caderno', 10, 'Estojo', 15, 'Mochila', 50,
            'Canetas', 12.90, 'Livro', 34.90)
print('-'* 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'* 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'* 40)

