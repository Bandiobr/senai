print("=== Lá no charuri ===")
print(" "*4, "Lanchonete" )

nome_cliente = input("Por favor, digite o seu nome: ")
print(f"Olá, {nome_cliente}")

print("=== NOSSO CARDAPIO ===")
print("1. Hamburguer Matador - R$ 39.59")
print("2. Coxinha Milanesa  -  R$ 38.53")
print("3. Pizza  Strognoff  -  R$ 40.20")

# Recebendo dados do pedido
print("\n Faça o seu pedido")
qtd_hamburguer = int(input("Quantos Hambúrguers você deseja?"))
qtd_coxinha = int(input("Quantas Coxinhas você deseja?"))
qtd_pizza = int(input("Quantas  Pizzas  você deseja?"))

#Fechando a conta 
total_hamburguer = qtd_hamburguer * 39.59
total_coxinha = qtd_coxinha * 38.53
total_pizza = qtd_pizza * 40.20
#Exibindo o cupom fiscal
print("\n" + "="*30)
print(" " * 8 + "CUPOM FISCAL" + " " * 8)
print("=" * 30)
print(f"Cliente: {nome_cliente}")
print(f"Hamburguer Matador: {total_hamburguer}")
print(f"Coxinha Milanesa: {total_coxinha}")
print(f"Pizza Strognoff: {total_pizza}")
print(f"Total do pedido: {total_hamburguer+ total_coxinha +total_pizza}")