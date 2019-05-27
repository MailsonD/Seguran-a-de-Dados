
matriz = []
tamanhoChave = 0


def showCript():
    chave = input("Informe uma chave: ")

    global tamanhoChave

    tamanhoChave = len(chave)

    constuirLinhaChave(chave)

    texto = input("Informe uma frase: ")

    texto = texto.replace(" ", "")

    construriMatriz(texto)

    print(cripto())


def showDecript():
    chave = input("Informe uma chave: ")

    global tamanhoChave

    tamanhoChave = len(chave)

    textoCriptografado = input("Informe o texto criptografado: ")

    print(decripto(textoCriptografado, chave))


def construriMatriz(text):
    linha = []
    limite = tamanhoChave
    if len(text) < tamanhoChave:
        limite = len(text)
    for i in range(0, limite):
        linha.append(text[i])
    if limite < tamanhoChave:
        for j in range(limite, tamanhoChave):
            linha.append("")

    matriz.append(linha)

    if len(text[tamanhoChave:]) > 0:
        construriMatriz(text[tamanhoChave:])


def constuirLinhaChave(chave):
    linhaChave = []
    for i in chave:
        linhaChave.append(i)
    matriz.append(linhaChave)


def formatarResultado():
    resultado = ""
    for i in matriz:
        for j in i:
            resultado += j
    return resultado


def cripto():
    ordem = sorted(matriz[0])
    numLinhas = len(matriz)
    resposta = ""
    for i in range(0, tamanhoChave):
        coluna = matriz[0].index(ordem[i])
        palavra = ""
        for j in range(1, numLinhas):
            palavra += str(matriz[j][coluna])
        resposta += palavra + " "
    return resposta


def buscarTamanhoMaiorPalavra(palavras):
    maior = len(palavras[0])
    for i in range(1,len(palavras)):
        if len(palavras[i])>maior:
            maior = len(palavras[i])
    return maior

def decripto(texto, chave):
    palavras = texto.split(" ")

    constuirLinhaChave(chave)

    ordem = sorted(matriz[0])
    tamanhoMaior = buscarTamanhoMaiorPalavra(palavras)
    for i in range(0, tamanhoMaior):
        matriz.append([])

    for i in range(0, tamanhoChave):
        palavra = palavras[ordem.index(chave[i])]
        for j in range(0, len(palavra)):
            matriz[j + 1].append(palavra[j])

    return formatarResultado()

print("Criptografar   - 1")
print("Decriptografar - 2")

try:
    choice = int(input())

    if choice == 1:
        showCript()
    elif choice == 2:
        showDecript()
    else:
        print("Valor inválido")

except TypeError as a:
    print("Unexpected error:", a.with_traceback())
    print("Valor inválido!")
