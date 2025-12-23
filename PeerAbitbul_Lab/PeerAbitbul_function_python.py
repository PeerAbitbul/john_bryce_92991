#function python
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Ex 1: Check if a number is even or odd
print("Ex 1: Check if a number is even or odd")

num = int(input("enter a number"))


def check(requst):
    if requst % 2 == 0:
        return 0
    else:
        return 1

print(check(num))

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 2: Calculate the average of a list of numbers
print("Ex 2: Calculate the average of a list of numbers")

number = int(input("how many numbers do you want to enter: "))

def average_of_numbers(number):
    input_numbers = list(map(int,input(f"enter {number} numbers separated by spaces: ").split()))
    return sum(input_numbers) / len(input_numbers)

final_average = average_of_numbers(number)
print(f"the average of the numbers is: {final_average}")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 3: Count the number of digits in a number
print("Ex 3: Count the number of digits in a number")

number = int(input("Enter a number (or -999 to stop): "))

def count_digits(n):
    s = str(n)
    if n < 0:
        return len(s) - 1
    else:
        return len(s)


while number != -999:
    result = count_digits(number)
    print(result)

    number = int(input("enter a number (or -999 to stop): "))


print("the user entered -999")


#more to leran function 
def sum_sum_digits(n):
    s = list(map(int,str(n)))
    result = sum(s)
    return result

num = int(input("Enter a number (0 to stop)"))

while num != 0:
    result = sum_sum_digits(num)


    print(f"The sum of digits is: {result}")
    num = int(input("Enter a number (0 to stop): "))

print("Goodbey")

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 4: 

change = int(input("insert a price: "))
original_price = change 

bills20 = change // 20      
print(f"{bills20} * 20 = {bills20 * 20}")
change = change % 20         


bills10 = change // 10      
print(f"{bills10} * 10 = {bills10 * 10}")
change = change % 10          


bills5 = change // 5       
print(f"{bills5} * 5 = {bills5 * 5}")
change = change % 5         

bills1 = change // 1          
print(f"{bills1} * 1 = {bills1 * 1}")

print("----------")
print(original_price)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 5: 


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# Ex 6: 
def dynamic_discount(dp):
    discount_requst = int(input("how many discount you want"))
    dp_result = dp * (1 - discount_requst/100)
    return dp_result

def static_discount(p):
    if p <= 1000:
        result = p - p * 0.10
        return result
    else:
        return dynamic_discount(p)
        

requst = int(input("insert price for check discount: "))
result = static_discount(requst)
print(f"the price is {result}")



