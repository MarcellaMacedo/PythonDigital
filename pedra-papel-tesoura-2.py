from random import randint

print('-' * 36)
comp = randint(0, 2)
print('\033[36mVamos jogar Jokenpô\033[m?')
print('''
(0)Pedra
(1)Papel
(2)Tesoura
''')
jog = int(input('Sua opção: '))
if jog == comp:
    print('\n\033[34mO jogo empatou =)\033[m!')

elif jog == 0 and comp == 2 or jog == 1 and comp == 0 or jog == 2 and comp == 1:
    print(f'\033[32mVocê escolheu {jog} e o computador {comp}, Você ganhou :D\033[m!!!')

elif jog > 2:
    print('\nSintaxe invalida, tente novamente!')

else:
    print(f'\n\033[31mO computador escolheu {comp} e você {jog}, você perdeu\033[m!')

