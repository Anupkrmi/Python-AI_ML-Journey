print("Loops in Python are used to execute a block of code repeatedly. There are two main types of loops in Python: for loops and while loops.")

print("For loops are used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
     print("The fruit is:", fruit)

print("While loops are used to execute a block of code as long as a condition is true.")
count = 0
while count < 5:
    print("The count is:", count)
    count += 1

print("You can use the 'break' statement to exit a loop prematurely.")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("The value of i is:", i)

print("You can use the 'continue' statement to skip the current iteration of a loop and move on to the next iteration.")
for i in range(10):
     if i % 2 == 0:
          print("Skipping the even number:", i)
          continue
     print("The odd number is:", i)

print("You can also use the 'else' statement with loops. The 'else' block will be executed when the loop is finished, unless the loop is terminated by a 'break' statement.")
for i in range(5):
    print("The value of i is:", i)
else:
    print("The loop has finished executing.")

print("Nested loops are loops within loops. You can use nested loops to iterate over multi-dimensional data structures.")
for i in range(3):
    for j in range(3):
        print("The value of i is:", i, "and the value of j is:", j)

print("You can use the 'pass' statement as a placeholder in loops. The 'pass' statement does nothing and is used when a statement is required syntactically but you do not want any code to be executed.")
for i in range(5):
    if i == 3:
        print("Using pass statement at i =", i)
        pass
    print("The value of i is:", i)

print("You can use the 'range()' function to generate a sequence of numbers for loops. The 'range()' function can take one, two, or three arguments: start, stop, and step.")
print("Using range() with one argument:")
for i in range(5):
    print("The value of i is:", i)

print("Using range() with two arguments:")
for i in range(2, 5):
    print("The value of i is:", i)

print("Usage of for and while loops are that for loops are generally used when the number of iterations is known, while while loops are used when the number of iterations is not known and depends on a condition.")

