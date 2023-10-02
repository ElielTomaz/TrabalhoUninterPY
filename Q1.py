#Recepção da loja
print('Bem Vindo a Loja do Eliel Tomaz de Aquino Filho!')
#Dados da compra
valor_produto = float(input('Digite o valor do produto: '))
quantidade = int(input('Digite quantos produtos foram comprados: '))
total_sem_des = valor_produto * quantidade
#variação de desconto
if(0 <= quantidade < 10):
    desconto = 0
elif(10 <= quantidade < 100):
    desconto = 0.05
elif(100 <= quantidade <1000):
    desconto = 0.1
else:
    desconto = 0.15
#Aplicando o desconto no valor final:
valor_final = total_sem_des - total_sem_des * desconto
#Informando o total da compra com e sem desconto:
print('O valor sem desconto foi: R$ {:.2f}'.format(total_sem_des))
print('O valor com desconto foi: R$ {:.2f}    (Desconto de {}%)'.format(valor_final, 100*desconto))