print('{:=^40}'.format('LOJAS MESBLA'))
preco = float(input('Precço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] Á VISTA DINHEIRO/CHEQUE
[2] Á VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X NO CARTÃO''')
opcao = int(input('Qual é a opção?'))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))


