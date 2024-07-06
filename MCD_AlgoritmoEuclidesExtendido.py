#Juan Carlos Vargas Castro

a = int(input("Dame el primer entero: "))
b = int(input("Dame el segundo entero: "))

q = a//b
r = a - b*q
while r != 0 :
  a = b
  b = abs(r)        #Agregué el absoluto del residuo para considerar enteros negativos
  print(a, b)
  q = a//b
  r = a - b*q
print("El máximo común divisor es: ", b)