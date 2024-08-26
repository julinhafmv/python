pagamentos = []

while True:
    print('0: Sair')
    print('1: Adicionar valor a ser pago')
    print('2: Remover pagamento')
    print('3: Vizualizar lista de pagamento')

    opcoes = input('Digite o número de pagamento:')

    if opcoes == '1':
        valor = input('Digite o pagamento')
        pagamento.append(valor)

    if opcoes == '2':
        print(pagamentos.pop(0))
        pagamento = float(input('Digite o valor que deseja pagar:'))

        if pagamento == pagamentos[0]:
            print(f'Cont no valor de {pagamentos.pop(0)} efetuado')
        else:
            print('Valor insuficiente')


    if opcoes == '3':
        print(f'{len(pagamentos)} - {pagamentos}')
    if opcoes == '0':
        break


    