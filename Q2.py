#Recepção na lanchonete
print('Bem Vindo a Lanchonete do Eliel Tomaz de Aquino Filho')
print(('*')*15+('Cardápio')+('*')*15)
print('| Código |        Descrição        |  Valor |')
print('|   100  |      Cachorro Quente    |   9,00 |')
print('|   101  | Cachorro Quente Duplo   |  11,00 |')
print('|   102  |           X-Egg         |  12,00 |')
print('|   103  |        X-Salada         |  12,00 |')
print('|   104  |         X-Bacon         |  14,00 |')
print('|   105  |         X-Tudo          |  17,00 |')
print('|   200  |     Refrigerante Lata   |   5,00 |')
print('|   201  |      Chá gelado         |   4,00 |')
#Valor da conta do cliente que mudará dependendo do pedido
pagar = 0
#Pedido do Cliente
while(True):
    c = int(input('Escreva o código do alimento desejado: '))
    if (c == 100):
        print('Você pediu um Cachorro Quente no Valor de R$ 9,00')
        pagar += 9.00
    elif (c == 101):
        print('Você pediu um Cachorro Quente Duplo no Valor de R$ 11,00')
        pagar += 11.00
    elif (c == 102):
        print('Você pediu um X-Egg no Valor de R$ 12,00')
        pagar += 12.00
    elif (c == 103):
        print('Você pediu um X-Salada no Valor de R$ 12,00')
        pagar += 12.00
    elif (c == 104):
        print('Você pediu um X-Bacon no Valor de R$ 14,00')
        pagar += 14.00
    elif (c == 105):
        print('Você pediu um X-Tudo no Valor de R$ 17,00')
        pagar += 17.00
    elif (c == 200):
        print('Você pediu um Refrigerante Lata no Valor de R$ 5,00')
        pagar += 5.00
    elif (c == 201):
        print('Você pediu um Chá Gelado no Valor de R$ 4,00')
        pagar += 4.00
    else:
        print('Opção Inválida!')
        continue #Volta para o começo do While caso o cliente digite um código inválido
    #Oferecer ao cliente a opção de comprar mais produtos
    print('Deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    mais_comida = int(input('>>>>>'))
    if(mais_comida == 1):
        continue
    else:
        #Valor final do pedido
        print('O total a ser pago é: R$ {:.2f}'.format(pagar))
        break