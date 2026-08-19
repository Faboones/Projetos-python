import os

palavra_chave = 'pira'
letra_digitada = ''
letra_certa = ''
tentativas = 0

while letra_certa != palavra_chave:

    letra_digitada = input ('Digite uma letra:')
    tentativas += 1

    if len(letra_digitada) > 1:
        print ('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_chave:
        letra_certa += letra_digitada

    palavra_certa = ''
    for letra in palavra_chave:
        if letra in letra_certa:
            palavra_certa += letra
        else:
            palavra_certa += '*'
    print (f'Palavra formada:{palavra_certa}')  

    if palavra_certa == palavra_chave:
        os.system('cls')
        print ('***PARABENS, VOCE CONSEGUIU!***')
        print (f'A palavra correta é: {palavra_chave}')
        print (f'Voce tentou {tentativas}x.')
        break               
