# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:  -à vista dinheiro/cheque:10%de desconto   -à vista no cartão:5% de desconto  -em até 2x no cartão:preço normal  -3x ou mais no cartãp:20%de juros

preco = float(input('Digite o preço do produto: '))
pagamento = int(input('Escolha a forma de pagamento: \n1)À vista no dinheiro/cheque\n2)À vista no cartão\n3)Em até 2x no cartão\n4)3x ou mais no cartão\nDigite o número da forma de pagamento: '))

if pagamento == 1:
    print('O valor final será R${} com 10% de desconto.'.format(preco-10/100*preco))
elif pagamento == 2:
    print('O valor final será R${} com 5% de desconto.'.format(preco-5/100*preco))
elif pagamento == 3:
    print('O valor final será R${}'.format(preco))
else:
    print('O valor final será R${} com 20% de juros.'.format(20/100*preco+preco))
