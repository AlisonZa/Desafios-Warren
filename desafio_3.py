# -*- coding: utf-8 -*-
"""Desafio 3 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdvQuKJAE6OSBzaIK4NROZual4IVD7Aq
"""

'''Importar o método combinations_with_replacement de itertools, o método realiza combinações repetindo o mesmo 
número varias vezes, mas não considera a lista com os mesmos elementos mas ordens diferentes como diferentes'''

from itertools import combinations_with_replacement

# Funções

# Valida se o input do usuário para o número a ser verificado é um número inteiro
def validarnumero(x):
  while x.isdecimal()==False or int(x)<0:
    print('Por gentileza digite um número inteiro positivo')
    x=(input('Digite o número, para o qual deseja encontrar as combinações: '))
  return int(x)

# Recebe os elementos, verifica se os mesmos são inteiros, e os armazena em uma lista.
def validar_lista(z):
  try:
      while True:
          z.append(int(input('O elemento da lista: ')))
          print('Para finalizar o lançamento dos elementos digite um número não inteiro ou qualquer letra ')
  except:
      pass
# Código

# Recebe o número n e o valida
n=input('Digite o número a serem verificadas as somas: ')
n= validarnumero(n)

# Recebe a lista de elementos a serem combinados e a valida
vetor=[]
validar_lista(vetor)

# Exibe na tela a lista de elementos
print(f'Os elementos a serem combinados são: {vetor}')

# Calcula o menor número na lista
menor = (min(vetor))

# Calcula o número máximo de loops que o laço for realizará
# O maior número de combinações possível será alcançado utilizando o menor elemento +1 para garantia
numlp = int((n/menor)+1)

# Definições das listas

# Lista que armazenará o conjunto, a diferença e a soma
la=[]

# Lista que armazena as diferenças
ldif=[]

#Coletar as combinações e as armazenar em uma lista
for i in range(0,numlp):
# Utiliza o método combinations_with_replacements com os elementos da lista percorrendo o número de loops máximo definido na variável 'numlp'.
  for a in combinations_with_replacement(vetor,i):

# Análise das diferenças entre sum(lista) e n:

# Converte as diferenças para números positivos, pois a distância de um número até a o outro é a mesma independente de a diferença ser positiva ou negativa
    s1=sum(a)
    diferenca= s1-n
    
    if diferenca<0:
       diferenca=(-diferenca)
    else:
      diferenca=(diferenca)  

# Armazena os dados do: conjunto, diferença e soma
    la.append((a,diferenca,s1))

# Percorre a 'la' armazenando o indíce [1] (diferença)
for x in la:
  ldif.append(x[1])

# Define o número de corte (menor diferença)
corte=min(ldif)

# Recebe as listas com diferenças [1] iguais ao corte
l2=[]

# Filtra as diferenças iguais ao corte
for x in la:
  if int(x[1])==corte:
    l2.append(x)
  else:
    pass

# Análise dos números de elementos:

# Recebe o número de elementos de cada lista
l3=[]

# Coletar o número de elementos de cada lista
for z in l2:
  l3.append(len(z[0])) 

# Recebe o menor número de elementos possível
nmin=(min(l3))

# Recebe a lista definitiva
l4=[]

#Corta as listas com mais elementos do que o necessário:
for u in l2:
  g=len(u[0])
  if g == nmin:
    l4.append(u)
  else:
    pass

# exibe os resultados na tela
print(f'\nPara o número {n} os resultados são os seguintes:\n')

for r in l4:
  print(f'Conjunto:{r[0]}')
  print(f'diferença:{r[1]}')
  print(f'Soma:{r[2]}\n')