#Largest prime factor
#n=50
n=600851475143
#n=13195
#Se hallaran los divisores menores a n/2 y se comprobara si son primos
N=0
k=2
for i in range(n/2,3,-2):
    print(i)
    if n%i==0:
        c=0
        for j in range(3,i/2,2):
            if i%j==0:
                c=c+1
        if c==0:
            N=i
            break


print(N)

#The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?
