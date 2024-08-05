######  Q.1 Write a program for arithmatic operators
## Arithmetic operators in Python

## Addition
def add(a, b):
    return a + b


## Subtraction
def subtract(a, b):
    return a - b


## Multiplication
def multiply(a, b):
    return a * b


## Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"


## Modulus
def modulus(a, b):
    return a % b


## Exponentiation
def exponentiate(a, b):
    return a ** b


## Floor Division
def floor_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Division by zero is not allowed"


## Example usage
num1 = 10
num2 = 3

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
print(f"{num1} % {num2} = {modulus(num1, num2)}")
print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
print(f"{num1} // {num2} = {floor_divide(num1, num2)}")

###### output
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.3333333333333335
# 10 % 3 = 1
# 10 ** 3 = 1000
# 10 // 3 = 3


##### Q.2 Write a program for assignment operators
# Assignment Operator
a = 3
b = 5
c = a + b
print(c)
#### output 8

a = 3
b = 5
# a = a - b
a -= b
print(a)
# Output
#### -2

##### Q.3Write a program for Bitwise operators
### And
a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)
#### output 0


# Print bitwise OR operation
a = 10
b = 4
print("a | b =", a | b)
##### output 14


###### Q.4 Write a program to calculate greatest of three numbers

a = 10
b = 20
c = 30
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b > c):

    largest = b
else:
    largest = (c)
print(" the laegest number is ", largest)

#### output 3o