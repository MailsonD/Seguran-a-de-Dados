# Armazena o tamanho da chave que será informada, para que seja possível
# gerar um keystream do tamanho da chave
tamanhoChave = 0
# Armazena o array que será utilizado para gerar o keystream
vetorInicial = []
# Armazena o tamanho do texto a ser cifrado
tamanhoTexto = 0


# Esta função inicializa o vetor para que seja possível gerar o keystream
# O vetor é preenchido com o intervalo [0,1,2...255]
def inicializarVetores(chave):
    global tamanhoChave
    tamanhoChave = len(chave)
    for i in range(0, 256):
        vetorInicial.append(i)


# Esta funcionalidade faz a permuta dos valores em duas posições específicas
# Do array, para que seja feita a dispersão
def permuta(posicao1, posicao2):
    aux = vetorInicial[posicao1]
    vetorInicial[posicao1] = vetorInicial[posicao2]
    vetorInicial[posicao2] = aux


# Esta funcionalidade é a primeira utilizada para gerar o keystream
# Ela tem como objetivo fazer a primeira dispersão dentro do array inicial
# É utilizado os valores do vetor de inicialização junto dos valores da chave (Em ASCII) para que seja feita a disperção
def ksa(chave):
    j = 0
    for i in range(0, 256):
        j = (j + vetorInicial[i] + ord(chave[i % tamanhoChave])) % 256
        # Utiliza de um indice pseudo-aleatório para que seja feita a permuta
        permuta(i, j)


# Esta funcionalidade é a segunda utilizada para gerar o keystream
# Ela percorre mais uma vez o array incial, porém agora aumentando o nível e dispersão
# Ela se utiliza de um novo vetor para que possa gerar o keystream, e garante que seja exatamente do mesmo
# tamanho do texto que ele deseja cifrar
def PRGA():
    ks = []
    j = 0
    for i in range(1, tamanhoTexto + 1):
        j = (j + vetorInicial[i]) % 256
        # Realiza novamente a permuta para que tenha uma maior dispersão
        permuta(i, j)
        # Atribui um indice pseudo-aleatório ao array utilizado para a keystream
        ks.append(vetorInicial[(vetorInicial[i] + vetorInicial[j]) % 256])
    return ks


# Esta função apenas organiza melhor a ordem dos passos a serem seguidos para se gerar
# O keystream
def keystream(chave):
    global tamanhoChave
    tamanhoChave = len(chave)
    inicializarVetores(chave)
    # Realiza a primeira dispersão
    ksa(chave)
    ks = ""
    # Depois a segunda
    # E ele vai ter um vetor equivalente a keystream (Em valores ASCII)
    for i in PRGA():
        # Ele converte a keystream em Caracteres, para que seja possível a visualização
        ks += chr(i)
    return ks


# Nesta funcionalidade ele faz o processo final da criptografia, onde ele faz o XOR
# Da keystrem pelo texto que deseja cifrar
def RC4(texto, ks):
    result = ""
    for i in range(0, tamanhoTexto):
        # Ele realiza o XOR e já converte o resultado de ASCII para Caractere
        result += chr(ord(texto[i]) ^ ord(ks[i]))
    return result


# Aqui é feito o uso do RC4 para cifrar o texto
def cripto(texto, ks):
    # A saída do texto cifrado é convertidad para hexa para que não se tenha problemas com caracteres
    # Que não são printáveis
    return RC4(texto, ks).encode("utf-8").hex()


# Aqui é feito o uso do RC4 para decifrar o texto
# Como a operação XOR é reversível quando aplicada novamente, basta utilizar a mesa funcionalidade
# Com o mesmo keystream, que será possível ter o resultado decifrado
def decripto(cr, ks):
    # É feita uma conversão de hexa para caractere normal, para que seja legível o resultado
    return RC4(bytes.fromhex(cr).decode("utf-8"), ks)


chave = input("Digite uma chave: ")
texto = input("Digite o texto: ")

tamanhoTexto = len(texto)

ks = str(keystream(chave))
cr = cripto(texto, ks)
dcr = decripto(cr, ks)

print("Keystream: " + ks.encode("utf-8").hex())
print("Cripto: " + cr)
print("Decripto: " + dcr)
