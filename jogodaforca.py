import random

palavras = ["luffy", "zoro", "sanji", "nami", "usopp", "chopper", "robin", "franky", "brook", "jinbe", "ace", "sabo",
"law", "kaido", "big mom", "blackbeard", "shanks", "kid", "doflamingo", "moriah", "boa hancock", "whitebeard", "mihawk", "crocodile",
"kuma","akainu", "aokiji", "fujitora", "ryokugyu", "kizaru", "garp", "roger", "rayleigh","dragon"]

def selecionar_palavra():
    return random.choice(palavras)

def desenhar_forca(erro):
    if erro == 0:
        print("  _______ ")
        print(" |/      |")
        print(" |      ")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif erro == 1:
        print("  _______ ")
        print(" |/      |")
        print(" |       O")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif erro == 2:
        print("  _______ ")
        print(" |/      |")
        print(" |       O")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|___")
    elif erro == 3:
        print("  _______ ")
        print(" |/      |")
        print(" |       O")
        print(" |       |/")
        print(" |")
        print(" |")
        print("_|___")
    elif erro == 4:
        print("  _______ ")
        print(" |/      |")
        print(" |       0")
        print(" |      \|/")
        print(" |")
        print(" |")
        print("_|___")
    elif erro == 5:
        print("  _______ ")
        print(" |/      |")
        print(" |       O")
        print(" |      \|/")
        print(" |       |")
        print(" |")
        print("_|___")
    else:
        print("  _______ ")
        print(" |/      |")
        print(" |       0")
        print(" |      \|/")
        print(" |       |")
        print(" |      / \\")
        print("_|___")

def iniciar_jogo():
    palavra_secreta = selecionar_palavra()
    letras_acertadas = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_chutadas = []

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Bem vindo ao Jogo da Forca - Especial One Piece")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")
    print("Vamos começar!")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    while tentativas > 0 and "_" in letras_acertadas:
        print("\nPalavra:", " ".join(letras_acertadas))
        print("Tentativas restantes:", tentativas)
        print("Letras chutadas:", letras_chutadas)

        letra_chutada = pedir_chute()

        if letra_chutada in letras_chutadas:
            print("Você já chutou essa letra. Tente novamente!")
            continue

        letras_chutadas.append(letra_chutada)

        if letra_chutada in palavra_secreta:
            atualizar_letras_acertadas(letra_chutada, palavra_secreta, letras_acertadas)
            print("Você acertou uma letra!")
        else:
            tentativas -= 1
            print("Você errou! Você tem", tentativas, "tentativas restantes.")
            desenhar_forca(6 - tentativas)

    if "_" not in letras_acertadas:
        print("\nParabéns! Você adivinhou a palavra secreta:", palavra_secreta)
    else:
        print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)
        desenhar_forca(6)

def pedir_chute():
    while True:
        letra = input("Digite uma letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite uma única letra.")
        else:
            return letra

def atualizar_letras_acertadas(letra, palavra_secreta, letras_acertadas):
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            letras_acertadas[i] = letra

iniciar_jogo()
