#Inicia o loop de calculadora
while True:

    #Pergunta se o usuario deseja fazer uma conta|| Se sim o loop da calculadora sera iniciado se nâo o loop cesssara aí mesmo
    y_n = input('deseja cnsultar uma tabuada? (responda com sim ou não) ')
    print("\n")
    
    #Avalia se  deve prosseguir com os calculos
    #Se sim inicia o processo da calculadora
    if y_n == 'sim':
        
        #inicia um loop para que seja dado um numero inteiro
        while True:
            #pede um número inteiro
            per_number_one = input('Digite um número inteiro: ')
            print("\n")

            #verifica se é um número inteiro
            if per_number_one.isnumeric():
                number_one = int(per_number_one)
                break
            #se não for dado um número inteiro pede para que seja escrito um número inteiro
            else:
                print('Você digitou algo que não se encaixa no pedido')
                print("\n")
                
        print(number_one,"x 1 =", number_one * 1)
        print(number_one,"x 2 =", number_one * 2)
        print(number_one,"x 3 =", number_one * 3)
        print(number_one,"x 4 =", number_one * 4)
        print(number_one,"x 5 =", number_one * 5)
        print(number_one,"x 6 =", number_one * 6)
        print(number_one,"x 7 =", number_one * 7)
        print(number_one,"x 8 =", number_one * 8)
        print(number_one,"x 9 =", number_one * 9)
        print(number_one,"x 10 =", number_one * 10)
        print("\n")
        
    elif y_n == 'não':
        print('Ok, até a proxima')
        print("\n")
        break
    else:
        print('Verifique se o que você digitou está igual as opições oferecidas')
        print("\n")