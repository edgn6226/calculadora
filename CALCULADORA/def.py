#pedir numeros
def pedir_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
                    print("Apenas números são validos\n")

# Operações

def  somar(b,c):
      return b + c

def subtrair(b,c):
      return b - c

def dividir(b,c):
      while True:
            try:
                return b / c
            except ZeroDivisionError:
                    print("Não é possível dividir por zero!\n")
                    c = pedir_numero("Digite o segundo número: \n")

def multiplicar(b,c):   
      return b * c

# Programa Principal

    #definir operação
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


b = pedir_numero("Digite o primeiro número: \n")
c = pedir_numero("Digite o segundo número: \n")

# Determinar função
if a == 1:
      resultado = somar(b,c)
elif a == 2:
      resultado = subtrair(b,c)
elif a == 3:
      resultado = dividir(b,c)
elif a == 4:
      resultado = multiplicar(b,c)

# Resultados
print (resultado)