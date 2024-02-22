import random
rando_number = random.randint(0,20)
chances = 0
max_try = 5

while chances < max_try:
    palpite = int(input("Voce possui 5 chances, use-as com moderação"))
    chances += 1
    
    if chances == rando_number:
        print("Parabens voce acertou!.")
        break
    
    elif  palpite < rando_number:
         print(f"Digite um numero maior que: {chances}")
    
    else:
        print(f"Digite um numero menor que:{chances}")
    if chances > max_try:
        print(f"Voce ainda tem {max_try - chances} rodadas")
    else:
        print(f"Voce nao conseguiu acertar. O numero era: {rando_number}")
        
print ("END GAME, THANKS")

    
    
    
    




