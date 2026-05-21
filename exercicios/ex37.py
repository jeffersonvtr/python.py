n = int(input("digit um numero inteiro: "))
choice = str(input('escolha entre bin, oct, hex: '))
if choice == 'bin':
 print(bin(n))
elif choice == 'oct':
 print(oct(n))
elif choice == 'hex':
 print(hex(n))
