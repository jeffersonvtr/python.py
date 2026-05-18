from datetime import date
ano =int(input("que ano quer analisar? coloque 0 para analisar ano atual"))
if ano == 0:
    ano = date.todey().year
    bissexto = ano % 4
    if bissexto == 0 and ano%100 != 0 or ano % 400 == 0:
        print("o ano {} é bissexual".format(ano))
    else:
        print("o ano {} não é bissexto".format(ano))
