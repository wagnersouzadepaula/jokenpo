import random

def imprimeCabecalhoJogo():
    print("*-"*20)
    print("|   [1]PEDRA, [2]TESOURA ou [3]PAPEL   |")
    print("*-"*20)


def jogarNovamente(escolha):
    if escolha == 1:
        return True
    else:
        return False


def escolhaDaMaquina():
    return random.randint(1, 3)


def escolhaDoUsuario():
    return int(input("Você vai jogar com [1] PEDRA, [2] TESOURA, [3] PAPEL: "))


def validaEscolhaDoUsuario(escolhaDoUsuario):
    if escolhaDoUsuario < 1 or escolhaDoUsuario > 3:
        print("[ERRO] Você deve escolher [1] PEDRA, [2] TESOURA ou [3] PAPEL: ")
        return True
    else:
        return False


def definirResultado(escolhaDaMaquina, escolhaDoUsuario):
    if escolhaDaMaquina == 1:
        if escolhaDoUsuario == 1:
            print(f"O computador e o usuário escolheram PEDRA, deu EMPATE")
        elif escolhaDoUsuario == 2:
            print(f"O computador escolheu PEDRA e você escolheu TESOURA. PEDRA quebra TESOURA. Você PERDEU!")
        elif escolhaDoUsuario == 3:
            print(f"O computador escolheu PEDRA e você escolheu PAPEL. PAPEL envolve PEDRA. Você GANHOU!")
    elif escolhaDaMaquina == 2:
        if escolhaDoUsuario == 2:
                print(f"O computador e o usuário escolheram TESOURA, deu EMPATE")
        elif escolhaDoUsuario == 1:
                print(f"O computador escolheu TESOURA e você escolheu PEDRA. PEDRA quebra TESOURA. Você GANHOU!")
        elif escolhaDoUsuario == 3:
                print(f"O computador escolheu TESOURA e você escolheu PAPEL. TESOURA corta PAPEL. Você PERDEU!")
    elif escolhaDaMaquina == 3:
        if escolhaDoUsuario == 3:
                print(f"O computador e o usuário escolheram PAPEL, deu EMPATE")
        elif escolhaDoUsuario == 2:
                print(f"O computador escolheu PAPEL e você escolheu TESOURA. TESOURA corta PAPEL. Você GANHOU!")
        elif escolhaDoUsuario == 1:
                print(f"O computador escolheu PAPEL e você escolheu PEDRA. PAPEL envolve PEDRA. Você PERDEU!")


def imprimeFimDoJogo():
    print("*-" * 10)
    print("|    FIM DE JOGO   |")
    print("*-" * 10)
