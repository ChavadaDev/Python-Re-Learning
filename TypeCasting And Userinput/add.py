# We'll create a simple program that will take two number as user input and add them together. We'll also take the user's name and greet them.

a = input("Enter your name: ") # Taking user input using input() function
print("Hello,", a) # Printing the user input
b = input("Enter first number: ") # Taking user input using input() function
c = input("Enter second number: ") # Taking user input using input() function

# NOTE: The input() function always returns a string. So, we need to convert the input to integer using int() function before performing addition.
d = int(b) + int(c) # Converting string to integer and adding them
print("The sum of", b, "and", c, "is:", d) # Printing the result of addition
print("Thank you for using our program,", a) # Printing a thank you message to the user