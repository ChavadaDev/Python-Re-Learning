print("We use double qoutes ' \"\"\" ' for normal print statements")
print('Same with single quotes " \'\'\' " for normal print statements')

# We can have all the valid data types printed in one single print statement like this
print("Hello my name is \"Dev\"", "My Age is", 25) # This is how we can use double quotes inside a string
# Also having comma "," in print statement will automatically add a space between the two strings or data types
print("hello")
print("hello", "world") # This will print hello world with a space in between

# Question: Can we override this behavior of adding space between the two strings or data types in print statement?
# Answer: Yes, we can override this behavior by using the 'sep' parameter in print statement. The 'sep' parameter is used to specify the separator between the two strings or data types in print statement. By default, the value of 'sep' parameter is a space " ". We can change it to any other character or string as per our requirement.

# Using 'sep' parameter in print statement
print("Hello", "World", sep="-") # This will print Hello-World with a hyphen in between
# Default value of 'sep' parameter is a space " ". We can change it to any other character or string as per our requirement.
# print("Dev you are so boring", end="") # This will print Dev you are so boring without a newline at the end
print("Dev you are so boring", end="0") # You can leave it as blank or you can put any other character or string as per your requirement. This will print Dev you are so boring without a newline at the end
print("This line will come after the previous line without a newline in between", end="''") # This will print This line will come after the previous line without a newline in between