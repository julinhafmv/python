mes = input("Digite um mes:")

if mes in("janeiro,fevereiro,março"):
    estacao = "Verão"
    
elif mes in("abril,maio,junho"):
    estacao = "outono"
    
elif mes in("julho,agosto,setembro"):
    estacao = "inverno"

elif mes in ("outubro,novembro,dezembro"):
    estacao = "primavera"
    

print(f"A estação do ano é: {estacao}")