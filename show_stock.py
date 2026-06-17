def show_stock(stock):
    print(f"""{'ID':<5} | {'Nome do produto':<10} | {'Quantidade':<10} | {'valor':<5}
    {'-' * 40}""")
    for id, product in stock.items():
        print(f"""{id:<5} | {product['nome']:<15} | {product['quantidade']:<10} | {product['valor']:<5}""")

