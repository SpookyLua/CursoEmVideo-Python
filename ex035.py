print('-=-'*15,'\nAnalisador de Triângulos')
print('-=-'*15)
l1=float(input('Primeiro Segmento: '))
l2=float(input('Segundo Segmento: '))
l3=float(input('Terceiro Segmento: '))

if l1 > l2+l3:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo.')
elif l2 > l1 + l3:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo.')
elif l3> l1 + l2:
    print('Os segmenots acima NÃO PODEM FORMAR um triangulo.')
else:
    print('Os segmentos acima PODEM FORMAR um triangulo')