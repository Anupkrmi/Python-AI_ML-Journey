print("Function is a block of code that is designed to perform a specific task. It can take inputs, process them, and return an output. Functions help in breaking down complex problems into smaller, manageable pieces, making the code more organized and reusable.")

def biggerNumber(a, b):
    """This function takes two numbers as input and returns the bigger number."""
    if a > b:
        return a
    else:
        return b

def oddEvenCheck(num):
    """This function checks if a number is odd or even."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("The bigger number between 10 and 20 is:", biggerNumber(10, 20))
print("The number 7 is:", oddEvenCheck(7))

print("Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller, similar subproblems. Recursion requires a base case to prevent infinite loops and ensure that the function eventually terminates.")

def factorial(n):
    """This function calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print("The factorial of 5 is:", factorial(5))

def fibonacci(n):
     """This function returns the nth Fibonacci number using recursion."""
     if n <= 0:  # Base case
          return 0
     elif n == 1:  # Base case
          return 1
     else:
          return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
     
print("The 7th Fibonacci number is:", fibonacci(7))

def sumOfDigits(n):
     """This function calculates the sum of digits of a number using recursion."""
     if n == 0:  # Base case
          return 0
     else:
          return n % 10 + sumOfDigits(n // 10)  # Recursive case

print("The sum of digits of 1234 is:", sumOfDigits(1234))

print("Built-in functions are pre-defined functions provided by Python that perform common tasks. They save time and effort as they eliminate the need to write code for frequently used operations. Some examples of built-in functions include print(), len(), type(), and range().")
print("The length of the string 'Hello' is:", len("Hello"))
print("The type of the variable 10 is:", type(10))
print("The range of numbers from 0 to 4 is:", list(range(5)))
print("The absolute value of -5 is:", abs(-5))

print("Parameterized functions are functions that accept parameters (inputs) to perform specific tasks. They allow you to pass different values to the function, making it more flexible and reusable. Parameters can be of any data type, including numbers, strings, lists, and even other functions.")

def greet(name):
    """This function greets a person with their name."""
    return f"Hello, {name}!"
print(greet("Alice"))

print("Default arguments are values that are assigned to function parameters if no argument is provided during the function call. They allow you to define functions with optional parameters, making the function more versatile.")

def greetWithDefault(name="Guest"):
    """This function greets a person with their name, or 'Guest' if no name is provided."""
    return f"Hello, {name}!"
print(greetWithDefault("Bob"))
print(greetWithDefault())  # No argument provided, uses default value
