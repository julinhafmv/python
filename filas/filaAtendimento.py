
atendimentos = ['manhã', 'tarde', 'noite']

while True:
    print('0: Sair')
    print('1: Adicionar horario de atendimento')
    print('2: Remover atendimento')
    print('3: Vizualizar atendimentos atuais')

    opcoes = input('Selecione: 0, 1 , 2 ou 3')

    if opcoes == '1':
        atendimento = input ('Digite o pedido')
        atendimento.append(atendimentos)
    if opcoes == '2':
        print(atendimento.pop(0))
    if opcoes == '3':
        print(f'{len(atendimentos)} - {atendimentos}')
    if opcoes == '0':
        break


