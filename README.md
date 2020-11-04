# Functions
## What are functions and why use them?
- Blocks of code that are built to do a single task
- Reusable so it follows the DRY principle (Don't Repeat Yourself)
- Instead of typing out the code to capitalise a string every time you want to do so, you can use the capitalise() function
- KISS (Keep it simple stupid), having code that does specific tasks makes your code simpler and cleaner
- Variables defined or changed in a function will not affect its value outside of that function
- This is because it is in local scope
## How to create the function
- Syntax is
```
def function_name(parameters_here):
    do_this
    maybe_return_this
```
- A simple example would be
```
def add2(num):
    result = num + 2
    return result
```
- A function definition should be followed by 2 blank lines
- For a function to run you have to call it
```
print(add2(5))
```
- Only when we called it did the code in the function run
- You can define a function with multiple arguments like below
```
# Create a new function that takes 2 arguments as ints and adds the value of the two args
def add(num1, num2):  # Takes two arguments
    print(num1 + num2)  # Print the result
```
## Tasks
### Task 1
- Task: Create a function to multiply (*)
```
def multiply(num1, num2):  # Defining the function with two arguments
    return num1 * num2  # Returning the value of one multiplied by the other
```
### Task 2
- Task: Create a function to do division (/)
```
def divide(num1, num2):  # Defining the function with two arguments
    return num1 / num2  # Returning the value of one divided by the other
```
### Task 3
- Task: Create a function to do modulo division (%)
```
def modulo(num1, num2):  # Defining the function with two arguments
    return num1 % num2  # Returning the value of one modulo the other
```
### Task 4
- Task: Create a function to do exponentials
```
def exponent(num1, num2):  # Defining the function with two arguments
    result = num1  # Creating the variable we wish to print
    for _ in range(num2 - 1):  # This loop will run for the amount of times stored in the num2 variable
        result = result * num1  # Multiplies the current value of the calculation with its original value
    return result  # Returning the final result
```