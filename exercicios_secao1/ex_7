lista_de_compras = []
while True:
  print("\nSelecione uma opção:")
  print("1 - Adicionar item")
  print("2 - Remover item")
  print("3 - Listar itens")
  print("4 - Sair\n")
  opcao = input("Opção: \n")
  if opcao == "1":
    item = input("Digite o item a ser adicionado: \n")
    lista_de_compras.append(item.capitalize())
    print("Item adicionado com sucesso!")
    continue
  if opcao == '2':
    item = int(input("Digite o item a ser removido: \n"))
    try:
      del lista_de_compras[item]
      print("Item removido com sucesso.")
    except:
      print("Item não encontrado na lista.")
      continue
  if opcao == '3':
    if len(lista_de_compras)==0:
      print("A lista está vazia.")
    for index, item in enumerate(lista_de_compras):
      print(index,'-', item)
  if opcao == '4':
    break
