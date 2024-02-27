def cadastrar_produto():
    marca = input("Digite a marca do produto: ")
    tipo = input("Digite o tipo do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    return {'marca': marca, 'tipo': tipo, 'preco': preco, 'quantidade': quantidade}

def salvar_produto(produto):
    with open('produtos.txt', 'a') as arquivo:
        arquivo.write(f"Marca: {produto['marca']}, Tipo: {produto['tipo']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}\n")
