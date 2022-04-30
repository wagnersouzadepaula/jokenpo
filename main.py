"""JOGO DE COMPUTADOR PARA JOGAR JOKENPO EM PYTHON."""

from funcoes import jogarNovamente, escolhaDaMaquina, escolhaDoUsuario, validaEscolhaDoUsuario, definirResultado, imprimeCabecalhoJogo, imprimeFimDoJogo

# MAIN
imprimeCabecalhoJogo()

joga_novamente = True

while jogarNovamente(joga_novamente):
    escolhaDaMaquina = escolhaDaMaquina()
    escolhaDoUsuario = escolhaDoUsuario()

    while validaEscolhaDoUsuario(escolhaDoUsuario):
        escolhaDoUsuario = escolhaDoUsuario()

    definirResultado(escolhaDaMaquina, escolhaDoUsuario)

    joga_novamente = int(input("Deseja jogar novamente? [1] SIM / [2] NÃO: "))

imprimeFimDoJogo()
