##Exercicio - sistema de perguntas e respostas

perguntas = [
  {
    'pergunta': 'Quanto é 2+2?',
    'opcoes': ['1','2','3','4'],
    'resposta': '4'
  },
  {
    'pergunta': 'Quanto é 4*4?',
    'opcoes': ['8','16','32','44'],
    'resposta': '16'
  },
  {
    'pergunta': 'Quanto é 3^2?',
    'opcoes': ['5','6','9','12'],
    'resposta': '9'
  }
]
acertos = 0
for numero_pergunta, pergunta in enumerate(perguntas):
  print("\nPERGUNTA: ", pergunta.get('pergunta'))
  opcoes = enumerate(pergunta['opcoes'])
  resposta_correta = 0
  for numero, opcao in opcoes:
    print(f'{numero})', opcao)
    if opcao == pergunta['resposta']:
      resposta_correta = str(numero)
  resposta = input("\n RESPOSTA: ")
  if resposta == resposta_correta:
    print("Resposta correta!")
    acertos += 1
  else:
    print("Resposta incorreta...")
print(f'\nVocê acertou {acertos} de {numero_pergunta+1}')