#Pregunta 1
def calcular_pi(n):
    sum = 0
    for i in range(1,n+1):
        sum += ((-1)**(i+1))/(2*i-1)
    return 4*sum


cantidad = input()
print(calcular_pi(int(cantidad)))

#Pregunta 2
def factorial(n):
    if n == 0:
      return 1
    return factorial(n-1)*n

def calcular_e(num):
    sum = 0
    for i in range(num+1):
      sum += 1/factorial(i)
    return sum

numero = input()
print(calcular_e(int(numero)))

#Pregunta 3
def divisores_propios(n):
  lista = [1]
  for i in range(2,n):
    if n%i == 0:
      lista.append(i)
  return lista

def amigos(num1,num2):
  sigmanum1 = sum(divisores_propios(num1))
  sigmanum2 = sum(divisores_propios(num2))
  if sigmanum1 == num2 and sigmanum2 == num1:
    return True
  return False

num1 = input()
num2 = input()
print(amigos(int(num1),int(num2)))

#Pregunta 4
def collatz(n):

  lista = [n]
  num = n
  i = 0
  while num != 1:

    if num%2 == 0:
      num = num/2
    else:
      num = 3*num + 1
    lista.append(int(num))
  return lista

numero = input()
print(collatz(int(numero)))

#Pregunta 5
def es_primo(n):
  if n == 1 or n == 2 or n ==3:
    return True
  for i in range(2,(int(n/2)+1)):
    if n%i == 0:
      return False
  return True

def lista_de_primos(n):
  lista = [2]
  for i in range(3,n+1):
    if es_primo(i):
      lista.append(int(i))
  return lista

def goldbash(n):
  lista = lista_de_primos(n)
  for i in lista:
    for j in lista:
      if i + j == n:
        return [i, j]

numero = input()
print(goldbash(int(numero)))