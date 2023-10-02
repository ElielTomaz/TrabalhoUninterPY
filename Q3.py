#Definindo a função dimensão do objeto
def dimensoesObjeto():
    while True:
        try:
            altura = float(input('Digite a altura do objeto (em cm): '))
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))
        except ValueError: #Mensagem caso o usuário digite um valor não numérico
            print('Você digitou um valor não numérico\nPor favor digite novamente.')
            continue
        volume = altura * comprimento * largura
        print('O volume do objeto é (em cm³): {:.2f}' .format(volume))
        if volume < 1000:
            return 10.00
        elif 1000 <= volume < 10000:
            return 20.00
        elif 10000 <= volume < 30000:
            return 30.00
        elif 30000 <= volume < 100000:
            return 50.00
        else: #Mensagem caso o volume seja acima de 100000 cm³
            print('Não aceitamos objetos com dimensões tão grandes\nEntre com as dimensões desejadas novamente.')

#Definindo a função peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): '))
        except ValueError: #Mensagem caso o usuário digite um valor não numérico
            print('Você digitou um valor não numérico\nPor favor digite novamente.')
            continue
        print('Peso do objeto (em kg): {}' .format(peso))
        if peso <= 0.1:
            return 1
        elif 0.1 < peso < 1:
            return 1.5
        elif 1 <= peso < 10:
            return 2
        elif 10 <= peso < 30:
            return 3
        else: #Mensagem caso o peso seja maior do que 30 quilos
            print('Não aceitamos objetos tão pesados\nDigite o peso novamente')

#Definindo a função rota do objeto, vou manter as siglas mas vou usar 2 cidades diferentes do exemplo (Recife,Salvador e Brasília)
def rotaObjeto():
    while True:
        try:
            rota = input('Selecione a rota:\nRS - De Recife para Salvador\nSR - De Salvador para Recife\nBS - De Brasília para Salvador\nSB - De Salvador para Brasília\nBR - De Brasília para Recife\nRB - De Recife para Brasília\n>>')
        except ValueError: #Caso seja digitado um valor númerico
            print('Você digitou um valor numérico\nPor favor entre com a rota desejada novamente')
            continue
        if rota == 'RS':
            return 1
        elif rota == 'SR':
            return 1
        elif rota == 'BS':
            return 1.2
        elif rota == 'SB':
            return 1.2
        elif rota == 'BR':
            return 1.5
        elif rota == 'RB':
            return 1.5
        else: #Mensagem caso o usuário digite a rota errada
            print('Você digitou uma rota que não existe\nPor favor entre com a rota desejada novamente')

#Programa principal
print('Bem vindo a Companhia de Logística Eliel Tomaz de Aquino Filho S.A')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
print('Total a pagar(R$): {:.2F}' .format(dimensoes * peso * rota))