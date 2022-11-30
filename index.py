#Suma de una serie de parametros

import sys
  
suma = 0  
nombre = sys.argv[0]
for i in sys.argv:
    if(nombre != i):
        print(i)
        #suma += int(i)

print(suma) 

