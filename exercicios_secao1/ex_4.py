numero = input("Digite um número: ")
try:
  if int(numero) % 2 == 0:
    print("O número é par.")
  else:
    print("O número é ímpar.")
except:
  print("O valor digitado não é um número.")
