import random

def jogar_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    placar_jogador = 0
    placar_computador = 0
    rodadas = 0

    print("\n=== PEDRA, PAPEL E TESOURA ===")
    print("Regras:")
    print("- Pedra vence tesoura")
    print("- Papel vence pedra")
    print("- Tesoura vence papel")
    print("- Digite 'sair' para encerrar o jogo\n")

    while True:
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if escolha_jogador == "sair":
            print("\n=== PLACAR FINAL ===")
            print(f"Você: {placar_jogador} vitórias")
            print(f"Computador: {placar_computador} vitórias")
            print(f"Total de rodadas: {rodadas}")
            print("Até a próxima! 👋")
            break

        if escolha_jogador not in opcoes:
            print("Escolha inválida! Tente novamente.\n")
            continue

        escolha_computador = random.choice(opcoes)
        rodadas += 1

        print(f"\nVocê escolheu: {escolha_jogador}")
        print(f"Computador escolheu: {escolha_computador}")

        # Lógica do jogo
        if escolha_jogador == escolha_computador:
            print("Empate! ⏸️")
        elif (
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel")
        ):
            print("Você ganhou! 🎉")
            placar_jogador += 1
        else:
            print("Você perdeu! 😢")
            placar_computador += 1

        print(f"Placar: Você {placar_jogador} x {placar_computador} Computador\n")

if __name__ == "__main__":
    jogar_pedra_papel_tesoura()