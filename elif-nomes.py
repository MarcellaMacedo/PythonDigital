nome = str(input('Qual é o seu nome?'))
if nome == 'Marcella':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'José' or nome == 'Paulo' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal...') #O else é opcional

print('Tenha um bom dia, {}!'.format(nome))


