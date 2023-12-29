import random

def jogar():
    imprimir_mensagem_apresentacao()

    palavra_secreta = gera_palavra_aleatoria()

    letras_acertadas = ["_" for letra in palavra_secreta] #LIST COMPREHENSIONS

    enforcou = False
    acertou = False
    erros = 0
    letras_chutadas = []

    while(not enforcou and not acertou):

        chute = pede_letra()

        if (chute not in letras_chutadas):
            letras_chutadas.append(chute)
        else:
            print("Você já digitou esta letra!")
            continue #ignora o resto do código abaixo e volta direto pro while

        if (chute in palavra_secreta):
            marca_letra_correta(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            informa_erros_e_chances(erros, palavra_secreta)

        acertou = "_" not in letras_acertadas
        enforcou = erros == len(palavra_secreta)

        informa_chutes_e_palavra_secreta(letras_acertadas, letras_chutadas)


    if (acertou):
        imprime_vitoria()

    else:
        imprime_derrota(palavra_secreta)


    print("Fim de jogo!")

def imprimir_mensagem_apresentacao():
    print("********************************")
    print("**Bem vindo ao Jogo da Forca!***")
    print("********************************\n")

#forma mais segura de abrir um arquivo, se houver algum erro durante a leitura e o programa parar,
#o arquivo poderia continuar aberto, já com essa sintaxe, esse problma foi resolvido
def gera_palavra_aleatoria():
    with open("palavras.txt", "r") as arquivo:
        lista_palavras = [palavra.strip() for palavra in arquivo]
    numero_aleatorio = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero_aleatorio].lower()
    return palavra_secreta

def pede_letra():
    chute = input("Digite uma letra: ")
    return chute.strip().lower()

def marca_letra_correta(chute, palavra_secreta, letras_acertadas):
    indice = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[indice] = letra
        indice += 1

def informa_erros_e_chances(erros, palavra_secreta):
    print(f"Você errou {erros} vez(es)!\n")
    print(f"Você tem {len(palavra_secreta) - erros} chances ainda!\n")

def informa_chutes_e_palavra_secreta(letras_acertadas, letras_chutadas):
    print(" ".join(letras_acertadas), end="\n\n")
    print(f"Letras chutadas: {", ".join(letras_chutadas)}")

def imprime_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_derrota(palavra_secreta):
    print("Você PERDEU!")
    print(f"A palavra era {palavra_secreta}!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()