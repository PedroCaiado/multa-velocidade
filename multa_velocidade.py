# Multa por excesso de velocidade: R$ 7,00 por km/h acima do limite.
limite = 80

while True:
    try:
        velocidade = float(input('Qual a velocidade do veículo? '))

        if velocidade <= 0:
            print('\033[33mA velocidade não pode ser negativa. Tente novamente.\033[m')
            continue  # volta para o início do loop

        break  # sai do loop se o valor for válido

    except ValueError:
        print('\033[31mEntrada inválida! Digite um número válido.\033[m')

if velocidade > 80:
    multa = (velocidade - 80) * 7
    excesso = velocidade - 80
    print('\033[31mVocê está {}Km/h acima da velocidade permitida e foi \033[4mMULTADO\033[0:31m no valor de R${}'.format(excesso, multa))
else:
    print('\033[32mVocê está na velocidade permitida, \033[4mparabéns\033[32m!')
print('\033[7;33mDirija com cuidado e tenha uma boa viagem!\033[m')