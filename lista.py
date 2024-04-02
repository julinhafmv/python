def incluir_item(lista):
    item = input("Digite o item que deseja incluir na lista: ")
    lista.append(item)
    print("Item incluído com sucesso!")

def excluir_item(lista):
    print("Lista atual:", lista)
    if len(lista) == 0:
        print("A lista está vazia.")
        return

    item = input("Digite o item que deseja excluir da lista: ")
    if item in lista:
        lista.remove(item)
        print("Item excluído com sucesso!")
    else:
        print("O item não está na lista.")

def visualizar_lista(lista):
    print("Lista atual:", lista)

def gravar_lista(lista):
    nome_arquivo = input("Digite o nome do arquivo para gravar a lista: ")
    with open(nome_arquivo, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("Lista gravada com sucesso no arquivo", nome_arquivo)

def carregar_lista():
    nome_arquivo = input("Digite o nome do arquivo a ser carregado:")
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista.clear()
            for linha in arquivo: 
                lista.append(linha.strip())
        print("Lista carregada co suceso.")

    except FileNotFoundError:
        print("arquivo não encontrado.")
    except Exception as e: 
        print("Ocorreu um erro".e)




def main():
    lista = []
    continuar = True

    while continuar:
        print("\n--- Menu ---")
        print("1. Incluir Item")
        print("2. Excluir Item")
        print("3. Visualizar Lista")
        print("4. Gravar Lista")
        print("5. Carregar   Lista")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            incluir_item(lista)
        elif opcao == '2':
            excluir_item(lista)
        elif opcao == '3':
            visualizar_lista(lista)
        elif opcao == '4':
            gravar_lista(lista)
        elif opcao == '5':
            print("Saindo do programa...")
            continuar = False
        elif opcao == '6':
            carregar_lista(lista)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()