import os
from functions_sales_system import show_stock, add_to_cart, clear_terminal, show_menu_input

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

dict_user_cart = {}
while True:
    user_input = show_menu_input()

    if user_input == 1:
        clear_terminal()
        print(f"{"Estoque":^44}")
        show_stock(dict_stock,"id","Nome do produto", "Quantidade","Valor")

    elif user_input == 2:
        clear_terminal()
        add_to_cart(dict_stock, dict_user_cart)

    elif user_input == 3:
        clear_terminal()

        if not dict_user_cart:
            print("O carrinho está vazio!!")
        else:
            print(f"{"Carrinho":^44}")
            show_stock(dict_user_cart,"id","Nome do produto", "Quantidade","Valor")

