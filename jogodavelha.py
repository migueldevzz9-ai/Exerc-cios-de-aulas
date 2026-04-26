tabuleiro = [" ", " ", " ",
             " ", " ", " ", 
             " ", " ", " "]
jogador = "X"

for rodada in range(9):
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

    pos = int(input(f"Jogador {jogador}, escolha (1-9): ")) - 1

    if tabuleiro[pos] == " ":
        tabuleiro[pos] = jogador
    else:
        print("Posição ocupada!")
        continue

    # verificação simples (só algumas condições)
    if tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador:
        print(f"Jogador {jogador} venceu!")
        break

    # troca jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"