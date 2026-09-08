# entradas

a=int(input("Digite qual operação quer realizar: \n"
             "ex.:\n"
              "1 = Adição\n"
              "2 = Subtração\n"
              "3 = Divisão\n"
              "4 = Multiplicação\n"
))

# verificação de operador

while a < 1 or a > 4:
    print("Valor invalido para operação! \n")

    a = int(input("Digite novamente uma opção valida: /n"
             "ex.:\n"
              "1 = Adição\n"
              "2 = Subtração\n"
              "3 = Divisão\n"
              "4 = Multiplicação\n"
))

# Depois de validar solicita os valores
b=int(input("Informe o primeiro valor da operação: \n"))
c=int(input("Informa o segundo valor da operação: \n"))

# condições
if a==1:
    adicao = b+c
    print(f"O resultado da operação é: {adicao}")

elif a==2:
    subtracao = b-c
    print(f"O resultado da operação é: {subtracao}")

elif a==3:
    divisao = b/c
    print(f"O resultado da operação é: {divisao}")

elif a==4:
    multiplicacao = b*c
    print(f"O resultado da operação é: {multiplicacao}")
