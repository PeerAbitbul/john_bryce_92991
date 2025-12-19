#python basics
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 1-2: Basic math with 6 and 2
print("Ex 1-2: Basic math with 6 and 2")

x = 6
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------


# Ex 3: Math with 2 and 0.5
print("Ex 3: Math with 2 and 0.5")

# x = 2
y = 5
print(x / y)
print(x // y)
print(x % y)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 4: Using 6 variables (a, b, c, d, e, f)
print("Ex 4: Using 6 variables (a, b, c, d, e, f)")

a = -81
b = 10
c = a + b   
d = a - b  
e = a * b  
f = int(a / b) 

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 5: Printing results in a table
print("Ex 5: Printing results in a table")

width = 5
print(f"{'a':<{width}}|{'b':<{width}}|{'c=a+b':<{width}}|{'d=a-b':<{width}}|{'e=a*b':<{width}}|{'f=a/b':<{width}}")
print("-" * 65)
print(f"{a:<{width}}|{b:<{width}}|{c:<{width}}|{d:<{width}}|{e:<{width}}|{f:<{width}}")
print("-----------------------------------------------------------------")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 6: Table using only 'c' for results
print("Ex 6: Table using only 'c' for results")

a = -81
b = 10
c = a + b

print(f"{a:<{width}}|", end="")
print(f"{b:<{width}}|", end="")

print(f"{c:<{width}}|", end="")

c = a - b
print(f"{c:<{width}}|", end="")

c = a * b
print(f"{c:<{width}}|", end="")

c = a / b
print(f"{c:<{width}}", end="")


print("\n ----------------------------------------------------------------")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 7: Sum of 3 numbers (3 variables)
print("Ex 7: Sum of 3 numbers (3 variables)")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = num1 + num2 + num3

print(f"The sum of {num1}, {num2} and {num3} is {result}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 8: Sum of 3 numbers (2 variables)
print("Ex 8: Sum of 3 numbers (2 variables)")

result = int(input("Enter the first number: "))
num = int(input("Enter the second number: "))
result += num
num = int(input("Enter the third number: "))
result += num

print(f"The result is {result}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 9: Sum of 5 numbers (2 variables + loop)
print("Ex 9: Sum of 5 numbers (2 variables + loop)")

result = 0
counter = 0
while counter < 5:
    result += int(input(f"Enter the {counter + 1} number: "))
    counter += 1

print(f"The result is {result}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 10: Big calculation (many variables)
print("Ex 10: Big calculation (many variables)")

result = 0
a = int(input("Enter nubmer to a variable: "))
b = int(input("Enter nubmer to b variable: "))
c = int(input("Enter nubmer to c variable: "))
d = int(input("Enter nubmer to d variable: "))
e = int(input("Enter nubmer to e variable: "))

result = (a + b - c) * d / e

print(f"The result is {result}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 11: Big calculation (only 2 variables)
print("Ex 11: Big calculation (only 2 variables)")

result = int(input("Enter value for a: "))

temp = int(input("Enter value for b: "))
result += temp

temp = int(input("Enter value for c: "))
result -= temp  

temp = int(input("Enter value for d: "))
result *= temp

temp = int(input("Enter value for e: "))
result /= temp

print(f"The result is {result}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 12: Calculate the square of a number
print("Ex 12: Calculate the square of a number")

num = int(input("Enter a number: "))
result = num * num
print(f"The result is {result} (using *)")

num = int(input("Enter a number: "))
result = num ** 2
print(f"The result is {result} (using **)")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 13: Calculate the square of a number 
print("Ex 13: Calculate the square of a number")

num = int(input("Enter a number: "))
result = num * num
print(f"The square of {num} is: {result} (using *)")

num = int(input("Enter a number: "))
result = num ** 2
print(f"The square of {num} is: {result} (using **)")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 14: 
print("Ex 14: ")



number_list = []
for i in range(3):
    number_list.append(int(input("Enter a number: ")))

width = 5
print(f"{'x':<{width}}|{'x*x':<{width}}|{'x**2':<{width}}")
print("-" * 10)
    
print(f"{number_list[0]:<{width}}|{number_list[0]*number_list[0]:<{width}}|{number_list[0]**2:<{width}}")     
print(f"{number_list[1]:<{width}}|{number_list[1]*number_list[1]:<{width}}|{number_list[1]**2:<{width}}")     
print(f"{number_list[2]:<{width}}|{number_list[2]*number_list[2]:<{width}}|{number_list[2]**2:<{width}}")     


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 15: Calculate the area of a right-angled triangle
print("Ex 15: Calculate the area of a right-angled triangle")

side_a = float(input("Enter a number for triangle: "))
side_b = float(input("Enter b number for triangle: "))

area = (side_a * side_b) / 2
print(f"The area of the triangle is: {area}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 16: Extract TAX amount from total price
print("Ex 16: Extract TAX amount from total price")

tax_percentage = 0.18
total_price = float(input("Enter the total price: "))
result = total_price / (1 + tax_percentage)
result = total_price - result
print(f"The TAX amount is: {result:.2f}") #give alot of numbers after the decimal point


result = float(input("Enter the total price: "))
result = result * (0.18 / 1.18) 
print(f"The TAX amount is: {result:.2f}")


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 17: Calculate the price with TAX
print("Ex 17: Calculate the price with TAX")

result = float(input("Enter the price without TAX: "))
result = result * 1.18
print(f"The price with TAX is: {result:.2f}")


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 18: Calculate the net price and TAX amount
print("Ex 18: Calculate the net price and TAX amount")

price = float(input("Enter the total price: "))
net = price / 1.18
print(f"The net price is: {net:.2f} and the TAX amount is: {price - net:.2f}")


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 19: Calculate the net price and TAX amount using ONLY one variable
print("Ex 19: Calculate the net price and TAX amount using ONLY one variable")

result = float(input("Enter the total price: "))
print(f"Net: {result / 1.18:.2f}, TAX: {result - (result / 1.18):.2f}")


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 20: Calculate the average of a list of numbers
print("Ex 20: Calculate the average of a list of numbers")

tested = [100,60,70,95,81]
print(sum(tested) / len(tested))
