largura=float(input('Largura da parede: '))
altura=float(input('Altura da parede: '))
dimensao=(f'{largura}x{altura}')
area=largura*altura
tinta=area/2
print(f'Sua parede tem a dimensão de {dimensao} e sua área é de {area}m².\nPara pintar essa parede, você precisará de {tinta}L de tinta.')