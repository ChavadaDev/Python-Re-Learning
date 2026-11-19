"""age = 2

if (age>18):
    print("You can vote.")
    print("You can also have driver's license.")


print("This line will always be printed. regardless of the age value.")
"""
# This is if statement without else statement. It will only execute the code block if the condition is true. If the condition is false, it will skip the code block and continue with the rest of the program.


# if and else together

"""
age = int(input("Enter your age:\n "))

if (age>18):
    print("You can vote.")
    print("You can also have driver's license.")
else:
    print("You are not eligible to vote.")
    print("You are also not eligible to have driver's license.")
"""

# Let's now see if, elif and else together


age = int(input("Enter your age:\n "))

if (age>21):
    print("You can vote.")
    print("You can also have driver's license.")
elif (age==18):
    print("You are eligible to vote but not eligible to have driver's license.")
elif (age>=18 and age<=21):
    print("You are an adult but not eligible for marriage.")
elif (age>=16 and age<18):
    print("You are eligible to have driver's license but not eligible to vote.")
else:
    print("You are not eligible to vote.")
    print("You are also not eligible to have driver's license.")