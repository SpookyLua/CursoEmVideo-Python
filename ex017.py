'''oposto=float(input('O valor do cateto oposto: '))
adjacente=float(input('O valor do cateto adjacente: '))
hip=(oposto**2+adjacente**2)**(1/2)
print(f'O valor da hipotenusa é de {hip:.2f}')'''

#ou

import math
oposto=float(input('O valor do cateto oposto: '))
adjacente=float(input('O valor do cateto adjacente: '))
hip=math.hypot(oposto, adjacente)
print(f'O valor da hipotenusa é de {hip:.2f}.')