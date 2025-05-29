horario= input("Digite um horário (hh-mm): ")
horas = horario[0] + horario [1]
minutos = horario[3] + horario[4]

if int(horas) < 12:
  print("Bom dia!")
elif int(horas) < 18:
  print("Boa tarde!")
elif int(horas) < 23:
  print("Boa noite!")
