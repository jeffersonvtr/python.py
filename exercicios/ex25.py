nome = str(input("digite seu nome completo")).strip()
dividido = nome.split()
print('seu 1° nome é {}'.format(dividido[0]))
print('seu 2° nome é {}'.format(dividido[len(dividido)-1]))
