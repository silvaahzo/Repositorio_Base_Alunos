"""tabela = {"alface": 0.45,
            "batata": 1.20,
            "tomate": 2.30,
            "feijão": 1.50}
print(tabela["alface"])
print(tabela["batata"])
print(tabela["tomate"])
print(tabela["feijão"])
tabela['limão'] = 0.30
print(tabela)
print("Manga" in tabela)
print("alface" in tabela)"""
estoque = {
    "tomate": [1000, 2.30]
    "alface": [500, 0.45]
    "batata": [2001, 1.50]
}
total = 0 
print("=== registro de vendas ===")
while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ").lower()
    
    if produto == "fim":
        break

    if produto not in estoque:
        print("produto não encontrado no estoque.")
        continue
    if quantidade > estoque [produto][0]:
        print("Estoque insuficiente disponivel: {estoque[produto][0]}")
        continue

    preco = estoque[produto][1]
    custo = preco * quantidade
    estoque[produto][0] -= quantidade 

    print(f"venda registrada: {produto} - {quantidade} x R$ {preco:.2f} = R$ {custo:.2f}\n")

    print(f"=== Estoque Atualizado ===")
    
