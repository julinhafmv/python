try:
    n1 = float (input ("Digite um número"))
    n2 = float (input ("Digite outro número"))
except ValueError:
            print("Digite novamente!")
            
soma = n1 + n2

print (f"A soma do numero {n1} e do numero {n2}, resulta em {soma}")