# Quadratic equation #
import cmath

num1 = 10
num2 = 100
num3 = 3

contuxa = (num2**2) - (4*num1*num3)



solpos = (-num2-cmath.sqrt(contuxa))/(2*num1)
solneg = (-num2+cmath.sqrt(contuxa))/(2*num1)

print (solpos,solneg)