
    # em desenvolvimento

n1 = int(input("Digite seu primeiro número"));
n2 = int(input("Digite seu segundo número"));
opção = 0

while opção != 5:
    print('''  [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] outros números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2


