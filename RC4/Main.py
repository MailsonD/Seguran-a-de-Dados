tamanhoChave = 0
vetorInicial = []
tamanhoTexto = 12


def inicializarVetores(chave):
    global tamanhoChave
    tamanhoChave = len(chave)
    for i in range(0, 256):
        vetorInicial.append(i)


def permuta(posicao1, posicao2):
    aux = vetorInicial[posicao1]
    vetorInicial[posicao1] = vetorInicial[posicao2]
    vetorInicial[posicao2] = aux


def ksa(chave):
    j = 0
    for i in range(0, 256):
        j = (j + vetorInicial[i] + ord(chave[i % tamanhoChave])) % 256
        permuta(i, j)


def PRGA():
    ks = []
    j = 0
    for i in range(1, tamanhoTexto + 1):
        j = (j + vetorInicial[i]) % 256
        permuta(i, j)
        ks.append(vetorInicial[(vetorInicial[i] + vetorInicial[j]) % 256])
    return ks


def keystream(chave):
    global tamanhoChave
    tamanhoChave = len(chave)
    inicializarVetores(chave)
    ksa(chave)
    ks = ""
    for i in PRGA():
        ks += chr(i)
    return ks


def cripto(texto, ks):
    result = ""
    for i in range(0, tamanhoTexto):
        result += chr(ord(texto[i]) ^ ord(ks[i]))
    return result


def decripto(cr, ks):
    result = ""
    for i in range(0, tamanhoTexto):
        result += chr(ord(cr[i]) ^ ord(ks[i]))
    return result


chave = input("Digite uma chave: ")

texto = input("Digite o texto: ")
tamanhoTexto = len(texto)

ks = str(keystream(chave))

cr = cripto(texto, ks)

dcr = decripto(cr, ks)

print("Keystream: " + ks)

print("Cripto: " + cr)

print("Decripto: " + dcr)
