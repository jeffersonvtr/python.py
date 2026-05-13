distancia = int(input('digite a distancia da sua viagem em KM: '))
if distancia <= 200:
    print('a sua viagem de {} vai custar {}'.format(distancia, distancia * 0.50))
else:
    print('a sua viagem de {} vai custar {}'.format(distancia, distancia * 0.45))
