times = ('Palmeiras', 'Flamengo','Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo',
'Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)

print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)

print(f'Os 4 últimos times são {times[-4:]}')
print('-='*15)

print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)

print(f'O Chapecoense está na {times.index("Chapecoense") +1}ª posição')
