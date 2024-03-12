import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel" , "tesoura"]
    print("Bem vindo ao jogo JOKENPO!")
    print("Escolha entre: pedra, papel ou tesoura.")

    while True: 
        escolha_jogador = input("Faça sua escolha:")

        if escolha_jogador not in opcoes:
            print("Escolha inválida, tente novamente.")
            continue 

        escolha_computador = random.choice(opcoes)
        print(f"A escolha do computador foi: {escolha_computador}")

        if escolha_jogador  == escolha_computador:
            print("o resultado do jogo é: EMPATE!")
        elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel")
        ):
            print("Você GANHOU")
            vitorias += 1
            print("Voce tem {vitorias} vitorias")

        else:
            derrota += 1

            print("Você PERDEU")

        jogar_novamente = input("Deseja jogar novamente?").lower()
        
        if jogar_novamente != "sim":
            break

if __name__ == "__main__":
    jogar_jokenpo()


