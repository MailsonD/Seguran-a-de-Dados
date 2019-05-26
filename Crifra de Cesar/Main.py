alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
tamanhoAlfa = len(alfabeto)


def getAlfaCifra(chave):
    alfaCifra = []
    for i in range(0, tamanhoAlfa):
        if chave >= tamanhoAlfa:
            chave %= tamanhoAlfa
        alfaCifra.append(alfabeto[chave])
        chave += 1
    return alfaCifra


def cifrar(chave, texto):
    alfabetoCifrado = getAlfaCifra(chave)
    resultado = ""
    for i in texto:
        if i == ' ' or not alfabeto.__contains__(i.lower()):
            resultado += i
        else:
            resultado += alfabetoCifrado[alfabeto.index(i.lower())]
    return resultado


def decifragem(chave, texto):
    alfabetoCifrado = getAlfaCifra(chave)
    resultado = ""
    for i in texto:
        if i == ' ' or not alfabeto.__contains__(i.lower()):
            resultado += i
        else:
            resultado += alfabeto[alfabetoCifrado.index(i.lower())]
    return resultado


def opcaoCifragem():
    chave = int(input("Digite uma chave: "))
    if chave < 0:
        raise Exception
    texto = input("Digite o texto que deseja cifrar: ")
    print(cifrar(chave, texto))


def opcaoDecifragem():
    chave = int(input("Digite uma chave: "))
    if chave < 0:
        raise Exception
    texto = input("Digite o texto que deseja decifrar: ")
    print(decifragem(chave, texto))


try:
    print("Cifragem    - 1")
    print("Decifragem  - 2")
    opcao = int(input())
    if opcao < 1 or opcao > 2:
        raise Exception
    elif opcao == 1:
        opcaoCifragem()
    else:
        opcaoDecifragem()
except Exception as error:
    print("Valor inválido!")
