prdt = float(input('digite o valor normal do seu produto: '))
opc = int((input('formas de pagamento, 1-dinheiro, 2-cartao 3-2x no cartao, 4-3x ou mais no cartao')))
if opc == 1:
    opc1 = prdt * 0.10
    print('com 10% de desconto fica: {:.2f}'.format(prdt - opc1))
elif opc == 2:
    opc2 = prdt * 0.05
    print('com 5% de desconto fica: {:.2f}'.format(prdt - opc2))
elif opc == 3:
    opc3 = prdt / 2
    print('vai ser duas parcelas e {:.2f}, sem juros'.format(opc3))
elif opc == 4:
    parcelas = int(input('digite o numero de parcelas: '))
    opc4 = prdt / parcelas
    print('o produto parcelado em {:.2f}, fica {:.2f}, sem juros'.format(parcelas, opc4))
    else:
    print('numero incorreto')
