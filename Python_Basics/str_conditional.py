str1 = "This is a string.\n\tWe are learning about strings in Python."
print(str1)

hello = "Hello"
world = "World"
print(hello + " " + world)

print("The length of the string is:", len(str1))
print("The string in uppercase is:", str1.upper())
print("The string in lowercase is:", str1.lower())
print("The string with title case is:", str1.title())
print("The string with capitalized first letter is:", str1.capitalize())
print("The string with swapped case is:", str1.swapcase())
print("The string with leading and trailing whitespaces removed is:", str1.strip())
print("The string with leading whitespaces removed is:", str1.lstrip())
print("The string with trailing whitespaces removed is:", str1.rstrip())
print("The string with replaced substring is:", str1.replace("string", "text"))
print("The string with substring removed is:", str1.replace("string", ""))
print("The string with substring replaced is:", str1.replace("string", "text", 1))
print("The string with substring removed is:", str1.replace("string", "", 1))
print("The string with substring replaced is:", str1.replace("string", "text", 2))
print("The string with substring removed is:", str1.replace("string", "", 2))
print("The count of the substring in the string is:", str1.count("string"))

print("Indexing in Python is used to access individual characters in a string.")
print("The first character of the string is:", str1[0])
print("The last character of the string is:", str1[-1])
print("Slicing in Python is used to access a range of characters in a string.")
print("The first 10 characters of the string are:", str1[:10])
print("The last 10 characters of the string are:", str1[-10:])

print("Conditional statements in Python are used to perform different actions based on different conditions.")
print("The string contains the word 'Python':", "Python" in str1)
print("The string does not contain the word 'Java':", "Java" not in str1)

age = int(input("Enter your age: "))
if(age >= 18):
    print("You are an adult.")
elif(age < 0):
    print("Age cannot be negative.")
else:
    print("You are not an adult.")

light = "green"

if (light == "green"):
    print("You can go.")
elif (light == "yellow"):
    print("You should slow down.")
elif (light == "red"):
    print("You should stop.")
else:
     print("Invalid traffic light color.")

print("Nesting in conditional statements is when you have an if statement inside another if statement.")

number = int(input("Enter a number: "))
if (number > 0):
    print("The number is positive.")
    if (number % 2 == 0):
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")




