#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91* 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Palindromo:
c=0
i=0
N=53423
while i==0:
    print(N)
    if N/10<1:
        i=1
    c=c+1
    N=N/10
for k in range (0,c):

print(c)
