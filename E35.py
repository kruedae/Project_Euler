#Ejercicio 35 Project Euler. Circular primes



N=719

#Busco si el numero es primo
c=0
i=2
while (c!=1 and i<N/2):
    if N%i==0:
        c=1
    i=i+1
print(c)
