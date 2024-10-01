limite=80
vel=float(input('Qual a velocidade atual do carro? '))
multa=(vel-limite)*7

if vel > limite:
    print(f'MULTADO! Voce excedeu o limite permitido que é {limite}Km/h\nVoce deve pagar uma multa de {multa}R$!')
print('Tenha um bom dia! Dirija com segurança!')
