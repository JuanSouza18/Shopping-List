Compras = []

def Menu():
    while True:
        print("--Lista de Compras--")
        print("1. Adicionar um Item")
        print("2. Exibir itens")
        print("3. Editar Itens")
        print("4. Excluir Itens")
        print("5. Sair")

        option = input("Digite qual função você deseja: ")

        if option == "1":
            print("Adicionar Item na lista")
            item = input("Qual Item deseja inserir: ")
            Compras.append(item)  # Fixed: append to Compras, not item
            print("Item Adicionado com sucesso")

        elif option == "2":
            print("Exibir lista de compras")
            for i, item in enumerate(Compras, 1):
                print(f"{i}. {item}")  # Fixed: use i instead of 1

        elif option == "3":
            print("Editar lista")
            print("Itens atuais:")
            for i, item in enumerate(Compras, 1):
                print(f"{i}. {item}")
            try:
                codigo = int(input("Digite qual o código do item que deseja editar: ")) - 1    
                if 0 <= codigo < len(Compras):
                    novo_item = input("Digite o novo valor: ")
                    Compras[codigo] = novo_item
                    print("Item editado com sucesso!")
                else:
                    print("Código inválido!")
            except ValueError:
                print("Digite um número válido!")

        elif option == "4":
            print("Excluir Item da lista")
            print("Itens atuais:")
            for i, item in enumerate(Compras, 1):
                print(f"{i}. {item}")
            try:
                codigo = int(input("Digite qual o código do item que deseja excluir: ")) - 1
                if 0 <= codigo < len(Compras):
                    removed = Compras.pop(codigo)
                    print(f"Item '{removed}' removido com sucesso!")
                else:
                    print("Código inválido!")
            except ValueError:
                print("Digite um número válido!")

        elif option == "5":
            print("Saindo do programa...")
            break  
        else:
            print("Opção inválida! Digite um número entre 1 e 5.")

Menu()