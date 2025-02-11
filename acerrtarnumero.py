import random
from random import randint
print('\nOlá seja bem vindo ao jogo de adivinhar número!')
print('\nEu, estou pensando em um número entre 1 e 100!')
print('\nVocê tem 5 chances para adivinhar o numero correto.')
print('\nPor favor, selecione o nível de dificuldade:')

print('1. Fácil (10 chances)')
print('2. Médio (5 chances)')
print('3. Difícil (3 chances)')

dificuldade = int(input('\nSelecione a sua dificuldade: '))
if dificuldade == 1:
        chances = 10
        print(f'\nOk, você escolheu a dificuldade fácil, você tem {chances} chances')
        print('\nVamos começar o jogo!')
elif dificuldade == 2:
        chances = 5
        print(f'Ok, você escolheu a dificuldade mediana você tem: {chances}')
        print('Vamos começar o jogo!')
elif dificuldade == 3:
        chances = 3
        print('Olha ai, desafiante hein. Então vamos iniciar o game na dificuldade difícil, você tem: ',chances)

lista_numeros = [randint(0,100)]
numero_escolhido = random.choice(lista_numeros)


while True:
    tentativa = int(input('Vamos lá, digite a sua tentativa: '))
    if tentativa >100:
         print('O número que você digitou está fora dos parâmetros (0-100)') 
         continue
    if tentativa > numero_escolhido:
        print('O número escolhido é menor do que', tentativa)
    elif tentativa < numero_escolhido:
         print('O número escolhido é maior que', tentativa)
    if tentativa == numero_escolhido:
         print('Parabéns, você acertou. O número era: ', numero_escolhido)
         break
        
    else:
        chances -=1
        print(f'Errado. Você ainda tem {chances} tentativas')
        print("----------------------")

    if chances == 0:
      print('Você perdeu, o jogo acabou.')
      break
      