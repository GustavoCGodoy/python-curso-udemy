##Funções

def criar_multiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print("Duplicado: ",duplicar(2))
print("Triplicado: ",triplicar(2))
print("Quadruplicado: ",quadruplicar(2))