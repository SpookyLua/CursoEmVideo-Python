valor=float(input('Valor da Casa: R$'))
sal=float(input('Sálario do Comprador: R$'))
ano=float(input('Quantos anos de financiamento? '))

prest=valor/(ano*12)
saldisc=sal*0.30

print('Para pagar uma casa de R${} em {:.0f} anos a prestação será de R${:.2f}.'.format(valor,ano,prest))

if prest > saldisc:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO!')