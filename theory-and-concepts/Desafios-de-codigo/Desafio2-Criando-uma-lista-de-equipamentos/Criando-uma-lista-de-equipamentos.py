# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicitar os itens ao usuário:
print("Insira uma lista com três itens:\n")

contador = 0
while (contador < 3):

# TODO: Solicite o item e armazena na variável "item":
  item = str(input(f"Item {contador + 1}: "))
  
# TODO: Adicione o item à lista "itens":
  itens.append(item)
  contador += 1

# Exibe a lista de itens
print("\nLista de Equipamentos:\n")  
for item in itens:
    
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
