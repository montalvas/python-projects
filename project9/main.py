'''
A ideia consiste em criar um sistema de compras em programação funcional
O usuario tem a opção de criar uma lista ou acessar uma já existente
Pode adicionar um produto (nome - quantidade - preço unitario)
e o sistema vai calcular o total
'''

def novo_produto():
    nome_produto = input("Informe o nome do produto: ")
    quantidade_produto = float(input("Quantidade do produto (kg, L): "))
    preco_unitario_produto = float(input("Preço unitário do produto R$: "))
    preco_total_produto = quantidade_produto * preco_unitario_produto
    lista_produtos.append([nome_produto, quantidade_produto, preco_unitario_produto, preco_total_produto])
    print("produto adicionado!\n")

def listar_produto():
    valor_total = 0
    if lista_produtos:
        print("LISTA DE COMPRAS:")
        print("{:^10} | {:^20} | {:^9} | {:^9} | {:^9}".format("ITEM", "NOME", "QUANT", "PRECO", "TOTAL"))
        for posicao, produto in enumerate(lista_produtos):
            print("{:^10} | {:^20} | {:^9} | {:^9} | {:^9}".format(posicao, produto[0], produto[1], produto[2], produto[3]))
            valor_total += produto[3]
        print("TOTAL R$ {:.2f}\n".format(valor_total))
    else:
        print("Nenhum produto na lista.")
    print()

def remover_produto():
    if lista_produtos:
        listar_produto()
        produto_removido = input("Selecione o produto a ser removido: ")
        for produto in lista_produtos:
            if produto_removido == produto[0]:
                lista_produtos.remove(produto)
                print("produto removido.\n")
                break
    else:
        print("Não há produtos a serem removidos.\n")

menu_compra = ['Novo produto', 'Listar produtos', 'Remover produto', 'Sair']
lista_produtos = []

while True:
    print("OPÇÕES DE COMPRA:")
    for chave, valor in enumerate(menu_compra):
        print(f"{chave + 1} - {valor}")
    
    opcao = 0
    
    try:
        opcao = int(input("\nOpção: "))
    except (TypeError, ValueError, EOFError):
        print("\nInsira uma opção válida.")
        
    if opcao == 1:
        novo_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        remover_produto()
    elif opcao == 4:
        print("Operação encerrada")
        break
    else:
        print("Opção inválida!")