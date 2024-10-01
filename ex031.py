distancia=float(input('Qual a distância da sua viagem? '))
print(f'Voce esta prestes a começar uma viagem de {distancia}Km.')

if distancia < 200:
    valor=distancia*0.50
else:
    valor=distancia*0.45

print(f'E o preço da sua passagem será de {valor:.2f}R$')