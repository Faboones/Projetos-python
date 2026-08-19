while True:
    sinal = input ('Qual operação iremos fazer? (+, -, *, /)')  
    numero_1 = input ('Digite um numero:')
    numero_2 = input ('Digite outro numero:')
    try:
        numero1 = float (numero_1)
        numero2 = float (numero_2)
    except:
        print ('Você não inseriu numeros.')
        continue
    if sinal == ('+'):
            print (numero1 + numero2)
    elif sinal == ('-'):
            print (numero1 - numero2)
    elif sinal == ('*'):
             print (numero1 * numero2)
    elif sinal == ('/'):
            print (numero1 / numero2)
    else:
            print ('Você não digitou um operador valido.')
    resposta = input ('Deseja encerrar? s/n ').lower().startswith('s')
    if resposta is True:
        break 
