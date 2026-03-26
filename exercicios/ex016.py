t = float(input('digite KM rodados com o carro alugado: '))
d = int(input('quantos dias usou: '))
dr = d * 60
kmr = 0.15 * t
print('no total, seu carro vai ficar {:.2f} pela diaria, {:.2f} por km, no total {:.2f}'.format(dr, kmr, dr + kmr))
