# Função para exibir o preço do celular escolhido
def exibir_preco(celular):
    if celular == "1":
        print("O preço do iPhone 14 é R$ 6999,99.")
    elif celular == "2":
        print("O preço do Galaxy S22 é R$ 4999,90.")
    elif celular == "3":
        print("O preço do Redmi Note 11 é R$ 1699,90.")
    elif celular == "4":
        print("O preço do Moto G60 é R$ 1799,00.")
    elif celular == "5":
        print("O preço do Realme 8 Pro é R$ 2199,99.")
    else:
        print("Opção inválida, por favor escolha um número entre 1 e 7.")

# Função principal para o menu
def menu():
    print("Bem-vindo à loja de celulares!")
    print("Escolha um celular para ver o preço:")
    print("1. iPhone 14")
    print("2. Galaxy S22")
    print("3. Redmi Note 11")
    print("4. Moto G60")
    print("5. Realme 8 Pro")
    
    celular = input("Digite o número do celular desejado (1-7): ")
    
    exibir_preco(celular)

menu()