nome=str(input('Digite seu nome: ')).strip()
separa=nome.split()

print(f'''Analisando deu nome...
Seu nome em maísculas é {nome.upper()}.
Seu nome em minusculas é {nome.lower()}.
Seu nome tem ao todo {len(nome)-nome.count(' ')} letras.
Seu primeiro nome é {separa[1]} e tem {len(separa[1])}.''')