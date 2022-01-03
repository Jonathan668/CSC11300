#Jonathan So 11300 Morning Session Assignment 2#

import math

#A#
def minutes_to_millisec (min):
    return min * 60000

print ("Convert Minutes to Milliseconds.")
min = int(input("Enter a Time in Minute: "))
millsec = minutes_to_millisec(min)
print(min, " converts to ", millsec, "Millisecond")

#B#
def average(sum):
    return sum / 2

test1 = int(input('Enter score 1: '))
test2 = int(input('Enter score 2: '))
sum = (test1 + test2)
print(average(sum))

#C#
from math import sqrt

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

discrim = b*b-4*a*c

if discrim > 0:

    x1 = (((-b)+sqrt(discrim))/(2*a))
    x2 = (((-b)-sqrt(discrim))/(2*a))
    print("The roots are: %f and %f" %(x1,x2))

elif discrim == 0:

    x =(-b)/2*a
    print("There is one root:",x)

else:

    print("No roots,discriminant<0.")

#D#
def k_to_r (float_kelvin):
    return ((kelvin - 273.15) * 0.8  )

print ("Convert Kelvin to Reaumur.")
kelvin = float(input("Enter temperature in Kelvin: "))
reaumur = k_to_r(kelvin)
print(kelvin, "Kelvin converts to ", reaumur , " Reaumur")

def r_to_c (float_reaumur):
    return (reaumur * 5/4 )

print ("Convert Reaumur to Celcius.")
reaumur = float(input("Enter temperature in Reaumur: "))
celcius = r_to_c(reaumur)
print(reaumur, "Reaumur converts to ", celcius , " Celcius")



#F#
def print_signs():
    print("^ - ^ - ^^ - ^ - ^^ - ^ - ^^ - ^ - ^^")
def print_i():
    print("i        i        i        i        i")
def print_square():
    print_signs()
    print_i()
    print_i()
    print_i()
    print_i()

print_square()
print_square()
print_square()
print_square()
print_signs()







