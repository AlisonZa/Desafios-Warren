# -*- coding: utf-8 -*-
"""Desafio 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12GGGJVYdpI3RIir4csbZcRUGM4U-gqXY
"""

# Funções

# Valida se o input do usuário para o limite minímo de alunos é um número inteiro positivo
def validarnumero(x):
  while x.isdecimal()==False or int(x)<0:
    print('Por gentileza digite um número inteiro positivo ')
    x=(input('Digite o número mínimo de alunos '))
  return int(x)

# Recebe os tempos de chegada, verifica se os mesmos são inteiros, e os armazena em uma lista.
def validar_lista(z):
  try:
      while True:
          z.append(int(input('Informe o horário de chegada do aluno:')))
          print('Para finalizar o lançamento dos horários digite um número não inteiro ou qualquer letra')    
  except:
      pass

# Código

n=input('Digite o número mínimo de alunos ')
horarios_de_chegada=[]

a=validarnumero(n)
validar_lista(horarios_de_chegada)

# Variáveis que armazenaram os números de alunos atrasados e assiduos
assiduos=0
atrasados=0

# Percorre a lista analisando se o aluno está ou não atrasado, e atualiza os contadores de atrasados e assiduos
for chegada in horarios_de_chegada:
  if chegada <=0:
    assiduos+=1
  else:
    atrasados+=1

print(f'\nOs horários de chegadas dos alunos são: {horarios_de_chegada}')

# Analisa se as condições para o não cancelamento da aula forma cumpridas
if int(assiduos) >= a:
  print('\nAula normal')
  print(f'{assiduos} chegaram no horário.\n{atrasados} chegaram atrasados.O mínimo é de {a} alunos.\nPortanto a aula não será cancelada')
else:
  print('\nAula cancelada')
  print(f'{assiduos} chegaram no horário.\n{atrasados} chegaram atrasados.O mínimo é de {a} alunos.\nPortanto a aula será cancelada')