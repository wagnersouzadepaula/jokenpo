"""JOGO DE COMPUTADOR PARA JOGAR JOKENPO COM VC."""
import random
print("*-"*10)
print("[1]PEDRA, [2]TESOURA ou [3]PAPEL")
print("*-"*10)
joga_novamente = 1
while joga_novamente == 1:
    pc_choice = random.randint(1,3)
    user_choice = int(input("Você vai jogar com [1] PEDRA, [2] TESOUZA, [3] PAPEL: "))
    while user_choice < 1 or user_choice > 3 :
        user_choice = int(input("[ERRO] Você deve escolher [1] PEDRA, [2] TESOUZA ou [3] PAPEL: "))
    if pc_choice == 1:
        if user_choice == 1 :
            print(f"O computador e o usuário escolheram PEDRA, deu EMPATE")
        elif user_choice == 2 :
            print(f"O computador escolheu PEDRA e você escolheu TESOURA. PEDRA quebra TESOURA. Você PERDEU!")
        elif user_choice == 3 :
            print(f"O computador escolheu PEDRA e você escolheu PAPEL. PAPEL envolve PEDRA. Você GANHOU!")
    elif pc_choice == 2:
        if user_choice == 2 :
                print(f"O computador e o usuário escolheram TESOURA, deu EMPATE")
        elif user_choice == 1 :
                print(f"O computador escolheu TESOURA e você escolheu PEDRA. PEDRA quebra TESOURA. Você GANHOU!")
        elif user_choice == 3 :
                print(f"O computador escolheu TESOURA e você escolheu PAPEL. TESOURA corta PAPEL. Você PERDEU!")
    if pc_choice == 3:
        if user_choice == 3 :
                print(f"O computador e o usuário escolheram PAPEL, deu EMPATE")
        elif user_choice == 2 :
                print(f"O computador escolheu PAPEL e você escolheu TESOURA. TESOURA corta PAPEL. Você GANHOU!")
        elif user_choice == 1 :
                print(f"O computador escolheu PAPEL e você escolheu PEDRA. PAPEL envolve PEDRA. Você PERDEU!")
    joga_novamente = int(input("Deseja jogar novamente? [1] SIM / [2] NÃO: "))

print("*-" * 10)
print("FIM DE JOGO")
print("*-" * 10)
