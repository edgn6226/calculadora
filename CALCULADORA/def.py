lista_de_numeros = []  # Lista que vai armazenar os números digitados


# Função responsável por verificar se o usuário digitou um número inteiro
def verificador_De_numero(mensagem):
    while True:
        try:
            # Mostra a mensagem e transforma a entrada em número inteiro
            return int(input(mensagem))
        except ValueError:
            # Caso o usuário digite algo que não seja um número
            print("Apenas números são validos\n")


# =========================
# Operações matemáticas
# =========================

# Função para realizar a soma dos números da lista
def somar(lista_de_numeros):
    return sum(lista_de_numeros)


# Função para realizar a subtração
def subtrair(lista_de_numeros):
    # O primeiro número será o valor inicial da subtração
    # Os demais números ficam armazenados em "resto"
    sub, *resto = lista_de_numeros

    # Percorre os demais números e realiza a subtração
    for numeros in resto:
        sub -= numeros

    # Retorna o resultado da subtração
    return sub


# Função para realizar a multiplicação
def multiplicar(lista_de_numeros):
    # O primeiro número será o valor inicial da multiplicação
    # Os demais números ficam armazenados em "resto"
    multip, *resto = lista_de_numeros

    # Percorre os demais números e realiza a multiplicação
    for numeros in resto:
        multip *= numeros

    # Retorna o resultado da multiplicação
    return multip


# Função para realizar a divisão
def dividir(lista_de_numeros):
    # O primeiro número será o valor inicial da divisão
    # Os demais números ficam armazenados em "resto"
    div, *resto = lista_de_numeros

    # Percorre os números que serão usados na divisão
    for numeros in resto:

        # Verifica se o número usado como divisor é zero
        while numeros == 0:
            print("Não é possível dividir por zero!")

            # Pede outro número ao usuário
            numeros = verificador_De_numero("Digite outro número: ")

        # Realiza a divisão
        div /= numeros

    # Retorna o resultado da divisão
    return div


# =========================
# Programa Principal
# =========================

# Solicita ao usuário qual operação ele deseja realizar
while True:
    try:
        requisecao = int(input(
            "Digite qual operação quer realizar: \n"
            "ex.:\n"
            "1 = Adição\n"
            "2 = Subtração\n"
            "3 = Divisão\n"
            "4 = Multiplicação\n"
        ))

        # Verifica se a opção escolhida está entre 1 e 4
        if requisecao < 1 or requisecao > 4:
            print("Valor invalido para operação! \n")

        else:
            # Se a opção for válida, sai do while
            break

    except ValueError:
        # Caso o usuário digite algo que não seja um número
        print("Apenas números são validos\n")


# Pergunta quantos números o usuário deseja utilizar
perguntas = verificador_De_numero(
    "Quantos números você gostaria de calcular?\n"
)


# Repete a pergunta de acordo com a quantidade escolhida
for i in range(perguntas):

    # Solicita cada número ao usuário
    numeros = verificador_De_numero(
        "Digite o número: \n"
        ""
    )

    # Adiciona o número digitado à lista
    lista_de_numeros.append(numeros)


# =========================
# Determinar função
# =========================

# Escolhe qual função será executada
# de acordo com a operação escolhida pelo usuário

if requisecao == 1:
    resultado = somar(lista_de_numeros)

elif requisecao == 2:
    resultado = subtrair(lista_de_numeros)

elif requisecao == 3:
    resultado = dividir(lista_de_numeros)

elif requisecao == 4:
    resultado = multiplicar(lista_de_numeros)


# =========================
# Resultado
# =========================

# Mostra o resultado da operação
print(resultado)
