from show_stock import show_stock
dict_stock = {
    1 : {"nome" : "dudu1",
         "valor": 1050,
         "quantidade" : 14
         },
    2 : {"nome" : "dudu2",
         "valor": 2050,
         "quantidade" : 141
         },
    3 : {"nome" : "dudu3",
         "valor": 3050,
         "quantidade" : 1414
         },
    4 : {"nome" : "dudu4",
         "valor": 4050,
         "quantidade" : 14141
         }
}
user_input = int(input("""
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
       Bem-Vindo(a) Loja Abóbora 
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
    [1]|Visualizar Estoque
    [2]|Adicionar Item ao Carrinho
    [4]|Finalizar Compra
    [0]|Sair do sistema
    """
     ))
if user_input == 1:
    show_stock(stock)

elif user_input == 2:
    print("os produtos disponiveis são:")
    show_stock(dict_stock)



