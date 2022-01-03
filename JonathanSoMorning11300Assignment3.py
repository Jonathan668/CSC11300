#Jonathan So 11300 Morning Session Assignment 3#

#1#
def collatz(n):
    if (n%2)==0:
        n = n/2
    else:
        n = 3*n+1
    print(n)
    if n!=1:
        collatz(n)

x = int(input("Enter a number: "))
print(x)
collatz(x)

#2#
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

if b == 0:
    print("Undefined")
else:
    print(a / b)

#3#
x = int(input("Enter a number:"))
n = 2

while(n*n <= x):
    if x % n:
        n=n+1
    else:
        x = x // n
        print(n)
if x>1:
    print(x)
    print("End of program")

#4#
def prime_numbers(x):
    for n in range(2, x+1):
        for i in range (2, n):
            if n % i == 0:
                break
        else: print(n)

print("All prime numbers less than or equal to this number are: ")
prime_numbers(9) #function call with 9 as argument#