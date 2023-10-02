#Criando o dicionário para armazenar os dados
lista_de_pecas = []
#Definindo a função cadastrar a peça
def cadastrarPeca(codigo_peca):
    print('Você selecionou a opção de Cadastrar Peças ')
    print('Código da peça {}.' .format(codigo_peca))
    nome = input('Entre com o NOME da peça: ')
    fabricante = input('Entre com o FABRICANTE da peça: ')
    valor = float(input('Entre com o VALOR(R$) da peça: '))
    dicionario_pecas = {'codigo': codigo_peca, 'nome': nome, 'fabricante': fabricante, 'valor': valor}#Dicionário
    lista_de_pecas.append(dicionario_pecas.copy())#Manipulando listas

#Definindo a função consultar peças
def consultarPeca():
    print('Você selecionou a opção de Consultar Peças ')
    while True:
        try:
            menu_consultar_peca = int(input('Escolha a opção desejada:\n1- Consultar todas as peças\n2-Consultar peças por código\n3-Consultar peças por fabricante\n4- Retornar\n>>'))
            if menu_consultar_peca == 1:
                for peca in lista_de_pecas: #Seleciona cada dicionário e coloca na lista
                    for key, value in peca.items(): #Seleciona e imprime na tela cada conjuto de chave e valor
                        print('{} : {}' .format(key, value))
                        print()

            elif menu_consultar_peca == 2:
                entrada_codigo = int(input('Digite o CÓDIGO da peça: '))
                for peca in lista_de_pecas:
                    if (peca['codigo'] == entrada_codigo): #Checa se existe o código no dicionário,caso haja, ele imprime
                        for key, value in peca.items():
                            print('{} : {}' .format(key, value))
                            print()

            elif menu_consultar_peca == 3:
                entrada_fabricante = input('Digite o FABRICANTE da peça: ')
                for peca in lista_de_pecas:
                    if(peca['fabricante'] == entrada_fabricante): #Checar se o fabricante existe no dicionário
                        for key, value in peca.items():
                            print('{} : {}' .format(key , value))
                            print()

            elif menu_consultar_peca == 4:
                return
            else:
                print('Erro!\nDigite uma das opções acima')
                continue
        except ValueError:
            print('Erro! Digite apenas valores numéricos inteiros!')
            continue

#Definindo a função remover peças
def removerPeca():
    print('Você selecionou a opção de Remover Peças ')
    entrada_remover = int(input('Digite o código da peça a ser removida: '))
    for peca in lista_de_pecas:
        if(peca['codigo'] == entrada_remover):
            lista_de_pecas.remove(peca)
            return

#Progama principal
print('Bem Vindo ao Controle de Estoque da Bicicletaria do Eliel Tomaz de Aquino Filho')
codigo_peca = 0 #variável contador para registrar as peças
while True:
    try:
        menu = int(input('Escolha a opção desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair\n>>'))
        if menu == 1:
            codigo_peca += 1
            cadastrarPeca(codigo_peca)
        elif menu == 2:
            consultarPeca()
        elif menu == 3:
            removerPeca()
        elif menu == 4:
            print('Programa encerrado!')
            break #Finaliza o programa
        else:
            print('Escolha apenas uma das opções acima')
            continue
    except ValueError:
        print('Erro! Digite apenas valores numéricos inteiros.')