import os
def clear_terminal():
    os.system('cls' if os.name == 'nt'
              else 'clear'
              )
def show_menu_input():
    user_input = int(input("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
               Bem-Vindo(a) Loja Abóbora 
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
            [1]|Visualizar Estoque
            [2]|Adicionar Item ao Carrinho
            [3]|Visualizar Carrinho
            [4]|Finalizar Compra
            [0]|Sair do sistema
            """
            ))
    return user_input


def show_stock(stock,column0,column_1, column_2,column_3 ):
    print(f"""{column0:<5} | {column_1:<10} | {column_2:<10} | {column_3:<5}
{'-' * 44}""")
    for id, product in stock.items():
        print(f"""{id:<5} | {product['nome']:<15} | {product['quantidade']:<10} | {product['valor']:<5}""")


def add_to_cart (dict_stock,dict_user_cart):
    print(f"{"Nossos Produtos":^44}")
    show_stock(dict_stock, "id", "Nome do produto", "Quantidade", "Valor")
    id = int(input("Digite o ID do produto: "))
    quantity = int(input("Digite a quantidade: "))

    if id in dict_stock:
        if quantity <= dict_stock[id]['quantidade']:
            dict_user_cart[id] = {
                "nome": dict_stock[id]['nome'],
                "valor": dict_stock[id]['valor'],
                "quantidade": quantity,
                "total": quantity * dict_stock[id]['valor']
            }
            print(f"{"Carrinho":^44}")
            show_stock(dict_user_cart, "ID", "Nome do produto", "Quantidade", "Total")

        else:
            print("nao tem")
