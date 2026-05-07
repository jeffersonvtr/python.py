frase = str(input('digite uma frase: ')).strip().upper()
print('a ltra A aparece {} vezes na frase'.format(frase.find('A')))
print('A primeira letra A apareceu na posição {}',format(frase.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('A')))
