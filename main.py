numero = int(input('Escolha um número para fazer a tabuada: '))
if (numero > 0) and (numero < 101):
    x = 0
    while (x < 10):
        x = x + 1
        res = numero*x
        print('{} X {} = {}' .format(numero,x,res))

else:
    print('Valor inválido!')
