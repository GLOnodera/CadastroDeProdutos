from produto import cadastrar_produto, salvar_produto

def main():
    while True:
        opcao = input("Deseja cadastrar um novo produto? (s/n): ").lower()
        if opcao == 's':
            produto = cadastrar_produto()
            salvar_produto(produto)
            print("Produto cadastrado com sucesso!")
        elif opcao == 'n':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, por favor digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()
