import os

def incluir_item(lista):
    item = input("Digite o item que deseja incluir na lista: ")
    lista.append(item)
    print("Item incluído com sucesso!")

def excluir_item(lista):
    if len(lista) == 0:
        print("A lista está vazia. Não há itens para excluir.")
        return

    print("Lista atual:", lista)
    item = input("Digite o item que deseja excluir da lista: ")
    if item in lista:
        lista.remove(item)
        print("Item excluído com sucesso!")
    else:
        print("O item não está na lista.")

def visualizar_lista(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
    else:
        print("Lista atual:", lista)

def gravar_lista(lista):
    if len(lista) == 0:
        print("A lista está vazia. Não há itens para gravar.")
        return

    nome_arquivo = input("Digite o nome do arquivo para gravar a lista: ")
    with open(nome_arquivo, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("Lista gravada com sucesso no arquivo", nome_arquivo)

def carregar_lista(lista):
    nome_arquivo = input("Digite o nome do arquivo para carregar a lista: ")
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("Lista carregada com sucesso do arquivo", nome_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao carregar o arquivo:", e)

def listar_arquivos_diretorio():
    diretorio = os.getcwd()  # Obtém o diretório atual do script
    arquivos = os.listdir(diretorio)  # Lista todos os arquivos no diretório
    print("Arquivos no diretório atual:")
    
    for arquivo in arquivos:
        print(arquivo)

#def listar_arquivos_diretorio(extensao=".txt"):
#    diretorio = os.getcwd()  # Obtém o diretório atual do script
#    arquivos = os.listdir(diretorio)  # Lista todos os arquivos no diretório
#    print(f"Arquivos .{extensao} no diretório atual:")
#    for arquivo in arquivos:
#        if arquivo.endswith(extensao):
#            print(arquivo)
            
def ordenar_lista(lista):
    if len(lista) == 0:
        print("A lista está vazia. Não há itens para ordenar.")
        return

    lista.sort()
    print("Lista ordenada com sucesso!")

def pesquisar_item(lista):
    if len(lista) == 0:
        print("A lista está vazia. Não há itens para pesquisar.")
        return

    item_pesquisar = input("Digite o item que deseja pesquisar na lista: ")
    ocorrencias = [indice for indice, item in enumerate(lista) if item == item_pesquisar]
    if len(ocorrencias) > 0:
        print("O item", item_pesquisar, "foi encontrado nas posições:", ocorrencias)
    else:
        print("O item", item_pesquisar, "não foi encontrado na lista.")

def contar_itens(lista):
    if len(lista) == 0:
        print("A lista está vazia. Não há itens para contar.")
        return

    item_contar = input("Digite o item que deseja contar na lista: ")
    contador = lista.count(item_contar)
    print("O item", item_contar, "aparece", contador, "vezes na lista.")

def limpar_lista(lista):
    if len(lista) == 0:
        print("A lista já está vazia.")
        return

    lista.clear()
    print("Lista limpa com sucesso!")

def main():
    lista = []
    continuar = True

    while continuar:
        print("\n--- Menu ---")
        print("1. Incluir Item")
        print("2. Excluir Item")
        print("3. Visualizar Lista")
        print("4. Gravar Lista")
        print("5. Carregar Lista")
        print("6. Visualizar Arquivos no Diretório")
        print("7. Ordenar Lista")
        print("8. Pesquisar Item")
        print("9. Contar Itens na Lista")
        print("10. Limpar Lista")
        print("11. Sair")

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
            carregar_lista(lista)
        elif opcao == '6':
            listar_arquivos_diretorio()
        elif opcao == '7':
            ordenar_lista(lista)
        elif opcao == '8':
            pesquisar_item(lista)
        elif opcao == '9':
            contar_itens(lista)
        elif opcao == '10':
            limpar_lista(lista)
        elif opcao == '11':
            print("Saindo do programa...")
            continuar = False
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
