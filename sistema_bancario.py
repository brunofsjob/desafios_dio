
# Funciona em versão python 3.10 ou em versão superior.

import os

QTD_SAQUE = 3
MAX_VALOR_SAQUE = 500

# Declarando variáveis
# tipo int
saldo = 0
deposito = 0
saque = 0
i = 0

extrato = {}

#tipo string
info = ''
string = '[Conta Bancária]'
titulo = string.center(32, '=')

n_invalido = 'Número inválido.'
ctrl_c = 'Operação cancelada pelo usuário.'
op_invalida = 'Opção inválida, tente novamente.'

# Laço infinito até opção 'q' ser selecionada
while True:

    os.system('clear')

    menu = f'''

    {titulo}

    (d) - Depositar
    (s) - Sacar
    (e) - Consultar extrato
    (q) - Sair

    {info}
    '''

    print(menu)

    try:
        op = str(input('    Escolha as opções disponiveis: '))

        match op:

            case 'd':

                deposito = int(input('\tDigite o valor do depósito: '))

                if deposito > 0:
                    saldo += deposito
                    info = f'Depósito no valor de R$ {deposito:.2f} realizado com sucesso!'
                    i += 1
                    extrato[i] = f'Depósitado R${deposito:.2f}'

                else:
                    info = 'Valor de depósito invalido.'
                
            case 's':

                if QTD_SAQUE > 0:
                    saque = int(input('\tDigite o valor do saque: '))

                    if saque <= MAX_VALOR_SAQUE:

                        if saque <= saldo:
                            saldo -= saque
                            info = f'Saque no valor de R$ {saque:.2f} realizado com sucesso!'
                            QTD_SAQUE -= 1
                            i += 1
                            extrato[i] = f'Sacado R$ {saque:.2f}'
                            continue
                        
                        else:
                            info = 'Não é possível realizar saque: saldo insuficiente.'
                            continue

                    else:
                        info= 'Valor de saque excede o limite de R$ 500,00.'
                        continue
                else:
                    info = 'Operação não realizada: limite máximo de saque diário excedido.'
                    continue

            case 'e':

                info = 'Extrato de operações: \n\t'
                
                for i in extrato.values():

                    info += f'\n\t{i}'
                
                info += f'\n\n\tSeu saldo é R$ {saldo:.2f}'

                continue
                # print('\nSeu saldo é R$ {saldo:.2f}')
                

            case 'q':
                info = ctrl_c
                print('\t\n    Operação encerrada.\n\n')
                break

            case _:
                raise ValueError
                continue
        

    except ValueError:
        info = op_invalida
        continue

    except KeyboardInterrupt:
        os.system('clear')
        print('\nOperação cancelada pelo usuário\n')
        break