a = 44
b = "44"
print(a, type(a))
print(b, type(b))

# Typecasting is a process of converting one data type to another data type. In Python, we can use built-in functions like int(), float(), str() to perform typecasting.

# Note: Typecasting can lead to loss of information or errors if the conversion is not possible.


# Example of typecasting from string to integer

c = int(b)  # converting string to integer
print(c, type(c))


# Example of typecasting from integer to string

d = str(a)  # converting integer to string
print(d, type(d))


# !Important! thing to check the type of any variable is to use the type() function. It returns the data type of the variable.