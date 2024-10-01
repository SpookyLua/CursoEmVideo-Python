import random
import time
lista=[0,1,2,3,4,5]
numRan=random.choice(lista)
print('-=-'*20,'\nVou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-'*20)
escolha=int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
time.sleep(2)

if escolha==numRan:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('OPS! Voce errou, tente denovo.')