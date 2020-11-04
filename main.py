# Let's create a function to greet a user
# Syntax for a function definition is def function_name(arugments_here):
def greeting(name):
    print(f"Welcome, {name}!")  # Code in a definition is indented


greeting("Helen")  # Calling our welcome function. The function will not run unless called


# My own example function
def add2(num):  # Function takes an argument
    result = num + 2  # It then adds two to the argument passed
    return result  # And returns the new number


print(add2(5))  # Testing our function, passing 5 as the parameter, it outputs 7 which is what we expect


# Create a new function that takes 2 arguments as ints and adds the value of the two args
def add(num1, num2):  # Takes two arguments
    print(num1 + num2)  # Print the result


add(8, 56)  # Calling our add function


# Creating another function that will subtract two arguments
def subtract(num1, num2):  # Defining the function with two arguments
    print(num1 - num2)  # Printing the value of one subtracted by the other


subtract(5, 2)  # Calling the function


# Task: Create a function to multiply (*)
def multiply(num1, num2):  # Defining the function with two arguments
    return num1 * num2  # Printing the value of one multiplied by the other


# Task: Create a function to do division (/)
def divide(num1, num2):  # Defining the function with two arguments
    return num1 / num2  # Printing the value of one divided by the other


# Task: Create a function to do modulo division (%)
def modulo(num1, num2):  # Defining the function with two arguments
    return num1 % num2  # Printing the value of one modulo the other


# Task: Create a function to do exponentials
def exponent(num1, num2):  # Defining the function with two arguments
    result = num1  # Creating the variable we wish to print
    for _ in range(num2 - 1):  # This loop will run for the amount of times stored in the num2 variable
        result = result * num1  # Multiplies the current value of the calculation with its original value
    return result  # Printing the final result


# These function calls check that the functions work as intended
print(multiply(5, 4))
print(divide(10, 3))
print(modulo(8, 3))
print(exponent(3, 3))
