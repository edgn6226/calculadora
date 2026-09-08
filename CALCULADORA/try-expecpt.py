# Calculadora com tratamento de excessão

while True:
    try:
        a=int(input(
            "Digite qual operação quer realizar: \n"
            "ex.:\n"
            "1 = Adição\n"
            "2 = Subtração\n"
            "3 = Divisão\n"
            "4 = Multiplicação\n"
        ))

    # verificação de operador

        if a < 1 or a > 4:
            print("Valor invalido para operação! \n") # Volta para as opções

        else:
            break # segue o programa

    except ValueError:
        print("Apenas números são validos\n")

# Depois de validar solicita os valores

while True:# restringe b a ser apenas numeros
    try:
        b=int(input("Informe o primeiro valor da operação: \n"))
        break
    except ValueError:
                print("Apenas números são validos\n")

while True: # restringe c a ser apenas numeros
    try:
        c=int(input("Informa o segundo valor da operação: \n"))
        break
    except ValueError:
                print("Apenas números são validos\n")

# condições
if a==1:
    adicao = b+c
    print(f"O resultado da operação é: {adicao}")

elif a==2:
    subtracao = b-c
    print(f"O resultado da operação é: {subtracao}")

elif a==3:
    while True: #tratando divisão por zero
        try:
            divisao = b/c
            print(f"O resultado da operação é: {divisao}")
            break
        except ZeroDivisionError:
            print("Não é possível dividir por zero!")

            c=int(input("Informa o segundo valor da operação: \n"))

elif a==4:
    multiplicacao = b*c
    print(f"O resultado da operação é: {multiplicacao}")