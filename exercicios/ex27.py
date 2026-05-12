from random import randint
from time import sleep
aleatorio = randint(0, 5)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('em que némero eu pensei'))
print('processando...')
sleep(1.5)
if aleatorio==jogador:
    print('parabens! você conseguiu')
else:
    print('ganhei, eu pensei no número {} e não o {}'.format(aleatorio, jogador))
