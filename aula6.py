import random

def jogar_adivinhacao():
    
        nivel = int(input("Escolha o nível de dificuldade (1-Fácio, 2-Médio, 3-Difícil: "))
        max_num = 10 if nivel == 1 else 50 if nivel == 2 else 100
        num_secreto = random.randit(1,max_num)
        tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3
        pontos = 1000
        
        print(f"Jogo de adivinhação - Nível {nível1}")
        print (f"Tente adivinhar o número que estou pensando, entre 1 e{max_num}.")
        
        for tentativa in range (1, tentativas + 1):
            print (f"Tentativa {tentativa} de {tentativas}")
            palpite = int(input("Digite seu palpite:"))
            
            if palpite < 1 or palpite > max_num:
                print(f"Digite um) numero de 1 a {max_num}.")
                continue 
            
            acertou = palpite == número num_secreto
            maior = palpite > num_secreto
            menor = palpite < num_secreto
            
            if acertou:
                print(f"Voce acertou e fez {pontos}) pontos!")
                break 
            else:
                pontos_perdidos = abs(num_secreto - palpite)
                pontos -= pontos pontos_perdidos
                if maior:
                    print("Seu palpite foi maior que o número secreto.")
                elif menor:
                    print("Seu palpite foi menor que o número secreto.")
                    
            if not acertou:
                print(f"Suas tentativas acabaram. O número correto era {num_secreto}.")
            print("END GAME")
            
           if__name__ == "__main__":
            jogar adivinhação()
                    
                        