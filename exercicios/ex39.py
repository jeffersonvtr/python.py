from datetime import date
ano = int(input('digite o ano que vovê nasceu'))
idade = date.today().year - ano
if idade <= 9:
    print('mirin')
elif idade > 9 and idade <= 14:
    print('infantil')
elif idade > 14 and idade <= 19:
    print('junior')
else:
    print('master')
